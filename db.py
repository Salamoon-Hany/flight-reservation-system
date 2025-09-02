import sqlite3

def get_conn():
    return sqlite3.connect("flysky_reservations.db")

def init_db():
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            passenger_name TEXT NOT NULL,
            flight_number TEXT NOT NULL,
            date TEXT NOT NULL,
            seat TEXT NOT NULL,
            destination TEXT NOT NULL,
            ticket_class TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# CRUD functions: add, get all, update, delete
def add_reservation(passenger_name, flight_number, date, seat, destination, ticket_class):
    conn = get_conn()
    c = conn.cursor()
    c.execute("INSERT INTO reservations (passenger_name, flight_number, date, seat, destination, ticket_class) VALUES (?, ?, ?, ?, ?, ?)",
              (passenger_name, flight_number, date, seat, destination, ticket_class))
    conn.commit()
    conn.close()

def get_reservations():
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM reservations")
    res = c.fetchall()
    conn.close()
    return res

def update_reservation(res_id, passenger_name, flight_number, date, seat, destination, ticket_class):
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
        UPDATE reservations
        SET passenger_name=?, flight_number=?, date=?, seat=?, destination=?, ticket_class=?
        WHERE id=?
    """, (passenger_name, flight_number, date, seat, destination, ticket_class, res_id))
    conn.commit()
    conn.close()

def delete_reservation(res_id):
    conn = get_conn()
    c = conn.cursor()
    c.execute("DELETE FROM reservations WHERE id=?", (res_id,))
    conn.commit()
    conn.close()