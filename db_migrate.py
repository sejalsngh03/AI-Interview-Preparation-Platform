#!/usr/bin/env python3
"""
Database backup and migration utility for AI Interview Prep.
Run this before deploying updates that might change the schema.
"""

import os
import sqlite3
import shutil
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "interview.db")
BACKUP_DIR = os.path.join(os.path.dirname(__file__), "backups")

def ensure_backup_dir():
    os.makedirs(BACKUP_DIR, exist_ok=True)

def backup_database():
    """Create a timestamped backup of the database."""
    ensure_backup_dir()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(BACKUP_DIR, f"interview_backup_{timestamp}.db")
    shutil.copy2(DB_PATH, backup_path)
    print(f"Backup created: {backup_path}")
    return backup_path

def check_schema():
    """Print current database schema."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT sql FROM sqlite_master WHERE type='table'")
    for row in c.fetchall():
        print(row[0])
    conn.close()

def count_records():
    """Print record counts for each table."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    tables = ['users', 'questions', 'interviews', 'answers']
    for table in tables:
        c.execute(f"SELECT COUNT(*) FROM {table}")
        count = c.fetchone()[0]
        print(f"{table}: {count} records")
    conn.close()

def migrate_add_column(table, column, col_type, default=None):
    """Add a column to a table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Check if column exists
    c.execute(f"PRAGMA table_info({table})")
    columns = [row[1] for row in c.fetchall()]
    
    if column not in columns:
        if default is not None:
            c.execute(f"ALTER TABLE {table} ADD COLUMN {column} {col_type} DEFAULT {default}")
        else:
            c.execute(f"ALTER TABLE {table} ADD COLUMN {column} {col_type}")
        conn.commit()
        print(f"Added column {column} to {table}")
    else:
        print(f"Column {column} already exists in {table}")
    
    conn.close()

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python db_migrate.py [backup|schema|count|migrate]")
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == "backup":
        backup_database()
    elif cmd == "schema":
        check_schema()
    elif cmd == "count":
        count_records()
    elif cmd == "migrate":
        # Example migrations - add as needed
        print("Running migrations...")
        # migrate_add_column("users", "avatar_url", "TEXT")
        # migrate_add_column("interviews", "duration_seconds", "INTEGER", "0")
        print("No pending migrations.")
    else:
        print(f"Unknown command: {cmd}")