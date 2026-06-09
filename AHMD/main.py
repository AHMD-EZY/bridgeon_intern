import sqlite3

DB = 'movies.db'

def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            showtime TEXT,
            price REAL,
            available_seats INTEGER
        )
    ''')
    # seed sample data if empty
    cur.execute('SELECT COUNT(*) FROM movies')
    if cur.fetchone()[0] == 0:
        cur.executemany('INSERT INTO movies (title, showtime, price, available_seats) VALUES (?,?,?,?)', [
            ('Action Film','2026-06-08 19:00',9.99,100),
            ('Comedy','2026-06-08 20:30',8.50,80),
            ('Sci-Fi','2026-06-08 21:00',10.00,120),
        ])
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print('Initialized', DB)
