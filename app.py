import os
import re
import json
import random
import sqlite3
from datetime import datetime
from functools import wraps

from flask import Flask, g, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from questions import QUESTIONS

# ---------------------------------------------------------------- config ---
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-change-me")

DB = os.path.join(os.path.dirname(__file__), "interview.db")

ROLES = ["Software Developer", "Web Developer", "Data Analyst", "ML Engineer", "Fresher (General)"]
CATEGORIES = ["Technical", "HR", "Behavioral", "Programming"]
LEVELS = ["Beginner", "Intermediate", "Advanced"]

SCHEMA = """
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT UNIQUE,
    password TEXT,
    created_at TEXT
);
CREATE TABLE IF NOT EXISTS questions(
    id INTEGER PRIMARY KEY,
    category TEXT,
    role TEXT,
    level TEXT,
    text TEXT,
    reference TEXT,
    keywords TEXT
);
CREATE TABLE IF NOT EXISTS interviews(
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    category TEXT,
    role TEXT,
    level TEXT,
    qids TEXT,
    created_at TEXT,
    status TEXT DEFAULT 'in_progress'
);
CREATE TABLE IF NOT EXISTS answers(
    id INTEGER PRIMARY KEY,
    interview_id INTEGER,
    question_id INTEGER,
    answer TEXT,
    score REAL,
    feedback TEXT
);
"""

# ------------------------------------------------------------- database ---
def db():
    if "db" not in g:
        g.db = sqlite3.connect(DB)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(_):
    conn = g.pop("db", None)
    if conn:
        conn.close()


def init_db():
    conn = sqlite3.connect(DB)
    conn.executescript(SCHEMA)
    if not conn.execute("SELECT 1 FROM questions").fetchone():
        conn.executemany(
            "INSERT INTO questions(category, role, level, text, reference, keywords) "
            "VALUES (?,?,?,?,?,?)",
            QUESTIONS,
        )
    conn.commit()
    conn.close()


# --------------------------------------------------------------- helpers ---
def login_required(f):
    @wraps(f)
    def wrapper(*a, **k):
        if "uid" not in session:
            return redirect(url_for("login"))
        return f(*a, **k)
    return wrapper


def clean(text):
    return re.sub(r"[^a-z0-9\s]", " ", (text or "").lower()).strip()


def evaluate(answer, reference, keywords):
    """Score 0-10 = 50% keyword coverage + 30% TF-IDF cosine similarity + 20% answer length."""
    a_clean = clean(answer)
    kw_list = [k.strip().lower() for k in keywords.split(",") if k.strip()]

    if not a_clean:
        return 0.0, ["No answer was submitted."]

    # 1. keyword coverage
    hits = [k for k in kw_list if k in a_clean]
    kw_score = (len(hits) / len(kw_list)) if kw_list else 0

    # 2. TF-IDF cosine similarity with the reference answer
    try:
        vec = TfidfVectorizer().fit_transform([a_clean, clean(reference)])
        sim_score = float(cosine_similarity(vec[0:1], vec[1:2])[0][0])
    except ValueError:
        sim_score = 0.0

    # 3. answer length (rewards a reasonably developed answer, caps at 40 words)
    word_count = len(a_clean.split())
    len_score = min(word_count / 40, 1.0)

    total = (0.5 * kw_score + 0.3 * sim_score + 0.2 * len_score) * 10
    total = round(max(0.0, min(10.0, total)), 1)

    missing = [k for k in kw_list if k not in hits]
    feedback = []
    if total >= 8:
        feedback.append("Strong answer — well aligned with the expected concepts.")
    elif total >= 5:
        feedback.append("Decent answer, but it can be more complete.")
    else:
        feedback.append("This answer needs significant improvement.")
    if missing:
        feedback.append("Consider mentioning: " + ", ".join(missing[:5]) + ".")
    if word_count < 15:
        feedback.append("Try to explain your answer in more detail.")

    return total, feedback


# ---------------------------------------------------------------- routes ---
@app.route("/")
def index():
    return redirect(url_for("dashboard") if "uid" in session else url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not name or not email or not password:
            flash("Please fill in all fields.", "error")
            return render_template("auth.html", mode="register")

        try:
            db().execute(
                "INSERT INTO users(name, email, password, created_at) VALUES (?,?,?,?)",
                (name, email, generate_password_hash(password), datetime.now().isoformat()),
            )
            db().commit()
        except sqlite3.IntegrityError:
            flash("An account with this email already exists.", "error")
            return render_template("auth.html", mode="register")

        flash("Account created. Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("auth.html", mode="register")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        user = db().execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()

        if user and check_password_hash(user["password"], password):
            session["uid"] = user["id"]
            session["name"] = user["name"]
            return redirect(url_for("dashboard"))

        flash("Invalid email or password.", "error")
        return render_template("auth.html", mode="login")

    return render_template("auth.html", mode="login")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/dashboard")
@login_required
def dashboard():
    uid = session["uid"]
    past = db().execute(
        "SELECT * FROM interviews WHERE user_id=? AND status='completed' ORDER BY created_at DESC",
        (uid,),
    ).fetchall()

    scores = []
    for iv in past:
        row = db().execute(
            "SELECT AVG(score) AS avg_score FROM answers WHERE interview_id=?", (iv["id"],)
        ).fetchone()
        scores.append(row["avg_score"] or 0)

    avg_overall = round(sum(scores) / len(scores), 1) if scores else None
    best = round(max(scores), 1) if scores else None

    return render_template(
        "dashboard.html",
        roles=ROLES, categories=CATEGORIES, levels=LEVELS,
        total=len(past), avg_overall=avg_overall, best=best,
        recent=list(zip(past[:5], [round(s, 1) for s in scores[:5]])),
    )


@app.route("/interview/new", methods=["POST"])
@login_required
def new_interview():
    category = request.form.get("category")
    role = request.form.get("role")
    level = request.form.get("level")
    count = int(request.form.get("count", 5))

    def fetch_ids(query, params):
        return [r["id"] for r in db().execute(query, params).fetchall()]

    # 1. exact match: this category + level, and either this role or a generic question
    ids = fetch_ids(
        "SELECT id FROM questions WHERE category=? AND level=? AND (role=? OR role='Fresher (General)')",
        (category, level, role),
    )

    # 2. not enough yet: widen to any role, same category + level
    if len(ids) < count:
        for qid in fetch_ids("SELECT id FROM questions WHERE category=? AND level=?", (category, level)):
            if qid not in ids:
                ids.append(qid)

    # 3. still not enough: widen to the whole category, any level
    if len(ids) < count:
        for qid in fetch_ids("SELECT id FROM questions WHERE category=?", (category,)):
            if qid not in ids:
                ids.append(qid)

    if not ids:
        flash("No questions available for that combination yet — try a different category.", "error")
        return redirect(url_for("dashboard"))

    random.shuffle(ids)
    actual_count = min(count, len(ids))
    ids = ids[:actual_count]

    if actual_count < count:
        flash(
            f"Only {actual_count} matching question{'s' if actual_count != 1 else ''} were available for "
            f"that exact combination, so we filled the rest with closely related questions.",
            "success",
        )

    cur = db().execute(
        "INSERT INTO interviews(user_id, category, role, level, qids, created_at) VALUES (?,?,?,?,?,?)",
        (session["uid"], category, role, level, json.dumps(ids), datetime.now().isoformat()),
    )
    db().commit()
    return redirect(url_for("interview", interview_id=cur.lastrowid, step=1))


@app.route("/interview/<int:interview_id>/<int:step>", methods=["GET", "POST"])
@login_required
def interview(interview_id, step):
    iv = db().execute(
        "SELECT * FROM interviews WHERE id=? AND user_id=?", (interview_id, session["uid"])
    ).fetchone()
    if not iv:
        flash("Interview session not found.", "error")
        return redirect(url_for("dashboard"))

    qids = json.loads(iv["qids"])
    total_steps = len(qids)

    if step < 1 or step > total_steps:
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        qid = qids[step - 1]
        q = db().execute("SELECT * FROM questions WHERE id=?", (qid,)).fetchone()
        answer = request.form.get("answer", "")
        score, feedback = evaluate(answer, q["reference"], q["keywords"])

        db().execute(
            "INSERT INTO answers(interview_id, question_id, answer, score, feedback) VALUES (?,?,?,?,?)",
            (interview_id, qid, answer, score, json.dumps(feedback)),
        )

        is_last = step >= total_steps
        if is_last:
            db().execute("UPDATE interviews SET status='completed' WHERE id=?", (interview_id,))
        db().commit()

        next_url = (
            url_for("result", interview_id=interview_id)
            if is_last else
            url_for("interview", interview_id=interview_id, step=step + 1)
        )

        return render_template(
            "feedback.html",
            question=q, answer=answer, score=score, feedback=feedback,
            step=step, total=total_steps, is_last=is_last, next_url=next_url,
        )

    qid = qids[step - 1]
    q = db().execute("SELECT * FROM questions WHERE id=?", (qid,)).fetchone()

    return render_template(
        "interview.html", interview=iv, question=q, step=step, total=total_steps
    )


@app.route("/result/<int:interview_id>")
@login_required
def result(interview_id):
    iv = db().execute(
        "SELECT * FROM interviews WHERE id=? AND user_id=?", (interview_id, session["uid"])
    ).fetchone()
    if not iv:
        flash("Interview session not found.", "error")
        return redirect(url_for("dashboard"))

    rows = db().execute(
        "SELECT a.*, q.text AS q_text FROM answers a JOIN questions q ON a.question_id=q.id "
        "WHERE a.interview_id=? ORDER BY a.id",
        (interview_id,),
    ).fetchall()

    detailed = []
    for r in rows:
        detailed.append({
            "question": r["q_text"],
            "answer": r["answer"],
            "score": r["score"],
            "feedback": json.loads(r["feedback"]),
        })

    overall = round(sum(d["score"] for d in detailed) / len(detailed), 1) if detailed else 0

    return render_template("result.html", interview=iv, detailed=detailed, overall=overall)


@app.route("/progress")
@login_required
def progress():
    rows = db().execute(
        "SELECT * FROM interviews WHERE user_id=? AND status='completed' ORDER BY created_at",
        (session["uid"],),
    ).fetchall()

    history = []
    for iv in rows:
        avg = db().execute(
            "SELECT AVG(score) AS avg_score FROM answers WHERE interview_id=?", (iv["id"],)
        ).fetchone()["avg_score"] or 0
        history.append({
            "id": iv["id"],
            "date": iv["created_at"][:10],
            "category": iv["category"],
            "role": iv["role"],
            "level": iv["level"],
            "score": round(avg, 1),
        })

    return render_template("progress.html", history=history)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
