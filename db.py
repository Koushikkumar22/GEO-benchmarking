import sqlite3

def init_db():
    conn = sqlite3.connect("geo.db")
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS responses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        prompt TEXT,
        engine TEXT,
        response TEXT
    )
    """)
    conn.commit()
    conn.close()

def save_response(prompt, engine, response):
    conn = sqlite3.connect("geo.db")
    c = conn.cursor()
    c.execute("INSERT INTO responses (prompt, engine, response) VALUES (?, ?, ?)",
              (prompt, engine, response))
    conn.commit()
    conn.close()
