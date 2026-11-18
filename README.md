# AI Interview Preparation Platform

A Flask-based web app for practicing technical, HR, behavioral and programming interviews, with AI/NLP-based answer evaluation (keyword coverage + TF-IDF cosine similarity + answer-length scoring).

Built for the MCA Mini Project synopsis — "AI Interview Preparation Platform".

## Features

- **User Authentication**: Registration and login with secure password hashing (werkzeug), password strength validation
- **Dashboard**: Average score, best score, recent sessions, and **in-progress interview resume**
- **Interview Setup**: Choose category, job role, difficulty level, question count
- **Step-by-step Interview Flow**: Progress indicator with question navigation
- **AI/NLP Answer Evaluation** (0–10 score):
  - Keyword coverage (50%)
  - TF-IDF cosine similarity with reference answer (30%)
  - Answer length reward (20%)
- **Per-question Feedback**: Score, constructive feedback, **visual keyword highlighting** (matched/missing)
- **Result Page**: Overall score, detailed breakdown per question with keyword analysis
- **Progress Tracking**: History table + **interactive charts** (score trend line chart, distribution doughnut chart)
- **Session Management**: Auto-cleanup of abandoned interviews (>24 hrs), CSRF protection
- **Production Ready**: Environment-based config, gunicorn WSGI, Render deployment config

## Project structure

```
ai-interview-prep/
├── app.py                 # Flask app: routes, auth, evaluation logic
├── questions.py           # Question bank (category, role, level, reference, keywords)
├── requirements.txt
├── wsgi.py                # Production WSGI entry point
├── render.yaml            # Render.com deployment config
├── .env.example           # Environment variable template
├── templates/
│   ├── base.html
│   ├── auth.html
│   ├── dashboard.html
│   ├── interview.html
│   ├── feedback.html
│   ├── result.html
│   └── progress.html
├── static/
│   └── style.css
└── interview.db           # created automatically on first run
```

## How to run (Development)

1. Open a terminal in this folder.
2. (Recommended) create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS/Linux
   ```
3. Copy `.env.example` to `.env` and set a secure `SECRET_KEY`:
   ```
   copy .env.example .env       # Windows
   cp .env.example .env         # macOS/Linux
   ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the app:
   ```
   python app.py
   ```
6. Open `http://127.0.0.1:5000` (or `http://0.0.0.0:5000`).

The SQLite database (`interview.db`) and its tables are created automatically the first time the app runs, and the question bank from `questions.py` is seeded into it.

## Adding more questions

Add new tuples to the `QUESTIONS` list in `questions.py`:

```python
("Category", "Role", "Level", "Question text", "Reference answer", "keyword1,keyword2,keyword3")
```

Delete `interview.db` and restart the app to reseed with the updated list (this will also clear any existing user accounts and history).

## Production Deployment (Render.com)

### Prerequisites
- GitHub account
- Render.com account (free tier available)

### Steps

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/ai-interview-prep.git
   git push -u origin main
   ```

2. **Deploy on Render**:
   - Go to https://dashboard.render.com
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Render will auto-detect `render.yaml` and configure:
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn wsgi:app`
     - **Environment**: Python 3.11
     - **Auto-generated SECRET_KEY** (secure)

3. **SQLite Persistence** (optional):
   - For production, consider adding a Render Disk:
     - In Render dashboard → your service → Disks → "Add Disk"
     - Name: `data`, Mount Path: `/opt/render/project/src/data`, Size: 1 GB
     - Uncomment the `disk` section in `render.yaml` and redeploy

### Environment Variables
| Variable | Description | Required |
|----------|-------------|----------|
| `SECRET_KEY` | Flask secret for sessions/CSRF | Yes (auto-generated on Render) |
| `FLASK_DEBUG` | Enable debug mode (`true`/`false`) | No (default: `false`) |
| `PORT` | Port to bind (Render sets automatically) | No |

## Local Production Test

Test the production WSGI server locally:
```bash
gunicorn wsgi:app
# Then open http://127.0.0.1:8000
```

## Security Notes

- All forms protected with CSRF tokens (Flask-WTF)
- Passwords hashed with scrypt (werkzeug)
- Password strength enforced: 8+ chars, uppercase, lowercase, digit, special char
- `SECRET_KEY` must be set via environment variable (no default)
- User answers auto-escaped in templates (XSS prevention)
- SQLite uses parameterized queries (SQL injection prevention)

## Evaluation Algorithm Details

The AI evaluator combines three techniques:

1. **Keyword Matching (50%)**: Percentage of expected keywords present in answer
2. **TF-IDF Cosine Similarity (30%)**: Semantic similarity to reference answer using scikit-learn
3. **Answer Length (20%)**: Rewards developed answers (caps at 40 words)

Score range: 0–10. Feedback includes matched/missing keywords and qualitative assessment.

## Tech Stack

- **Backend**: Flask 3, Python 3.11+
- **Database**: SQLite (development), PostgreSQL recommended for production scale
- **ML/NLP**: scikit-learn (TF-IDF, cosine similarity)
- **Security**: Flask-WTF (CSRF), werkzeug (password hashing)
- **Frontend**: Vanilla HTML/CSS/JS, Chart.js (progress charts)
- **Deployment**: gunicorn, Render.com

## License

MCA Mini Project — Educational use.