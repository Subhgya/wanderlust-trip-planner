import sqlite3

def get_db():
    conn = sqlite3.connect("trips.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''
    CREATE TABLE IF NOT EXISTS trips (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        trip_name TEXT,
        destination TEXT,
        start_date TEXT,
        end_date TEXT,
        budget TEXT,
        travelers INTEGER,
        travel_style TEXT,
        notes TEXT
    )
    ''')
    conn.commit()
    conn.close()