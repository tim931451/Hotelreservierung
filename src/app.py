import sqlite3
import pandas as pd

DB_PATH = "data/hotel_reservation.db"

def show_all_hotels():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM hotels", conn)
    conn.close()
    print(df)

def filter_by_city():
    city = input("Gib eine Stadt ein: ")
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT * FROM hotels WHERE city = ?"
    df = pd.read_sql_query(query, conn, params=(city,))
    conn.close()
    print(df)

def add_hotel():
    name = input("Hotelname: ")
    city = input("Stadt: ")
    stars = input("Sterne (1–5): ")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO hotels (name, city, stars) VALUES (?, ?, ?)", (name, city, stars))
    conn.commit()
    conn.close()
    print("Hotel hinzugefügt!")

def main():
    while True:
        print("\nHotelmenü")
        print("1 = Alle Hotels anzeigen")
        print("2 = Nach Stadt filtern")
        print("3 = Neues Hotel hinzufügen")
        print("0 = Beenden")

        choice = input("Wähle eine Option: ")

        if choice == "1":
            show_all_hotels()
        elif choice == "2":
            filter_by_city()
        elif choice == "3":
            add_hotel()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Ungültige Eingabe!")

if __name__ == "__main__":
    main()