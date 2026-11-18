# AI Interview Preparation Platform

A Flask-based web app for practicing technical, HR, behavioral and programming
interviews, with AI/NLP-based answer evaluation (keyword coverage + TF-IDF
cosine similarity + answer-length scoring).

Built for the MCA Mini Project synopsis — "AI Interview Preparation Platform".

## Features

- User registration and login (hashed passwords via werkzeug)
- Dashboard with average score, best score, and recent sessions
- Interview setup: choose category, job role, difficulty level, question count
- Step-by-step interview flow with a progress indicator
- AI/NLP answer evaluation (0–10 score) using scikit-learn's `TfidfVectorizer`
  and cosine similarity, plus keyword-coverage and answer-length checks
- Per-question feedback (missing keywords, general remarks)
- Result page with overall score and detailed feedback
- Progress-tracking page showing history of all completed interviews

## Project structure

```
ai-interview-prep/
├── app.py                 # Flask app: routes, auth, evaluation logic
├── questions.py            # Question bank (category, role, level, reference, keywords)
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── auth.html
│   ├── dashboard.html
│   ├── interview.html
│   ├── result.html
│   └── progress.html
├── static/
│   └── style.css
└── interview.db            # created automatically on first run
```

## How to run

1. Open a terminal in this folder.
2. (Recommended) create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS/Linux
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the app:
   ```
   python app.py
   ```
5. Open the URL shown in the terminal (usually `http://127.0.0.1:5000`).

The SQLite database (`interview.db`) and its tables are created automatically
the first time the app runs, and the question bank from `questions.py` is
seeded into it.

## Adding more questions

Add new tuples to the `QUESTIONS` list in `questions.py`:

```python
("Category", "Role", "Level", "Question text", "Reference answer", "keyword1,keyword2,keyword3")
```

Delete `interview.db` and restart the app to reseed with the updated list
(this will also clear any existing user accounts and history).
