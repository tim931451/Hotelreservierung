import sqlite3

def connect_db(db_path="data/hotel_reservation.db"):
    """Stellt eine Verbindung zur SQLite-Datenbank her"""
    connection = sqlite3.connect(db_path)
    return connection
    def setup_database():
    """Erstellt die Tabelle 'hotels' und fügt Testdaten ein"""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hotels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            city TEXT NOT NULL,
            stars INTEGER
        )
    """)

    hotels = [
        ("Hotel Arosa", "Zürich", 4),
        ("Bergblick", "Bern", 3),
        ("Sonnenhof", "Luzern", 5)
    ]

    cursor.executemany("INSERT INTO hotels (name, city, stars) VALUES (?, ?, ?)", hotels)
    conn.commit()
    conn.close()