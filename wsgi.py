import os
from dotenv import load_dotenv

load_dotenv()

# Set database path for production (Render disk)
if os.environ.get("RENDER"):
    os.environ["DB_PATH"] = "/opt/render/project/src/data/interview.db"

from app import app, init_db

init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))