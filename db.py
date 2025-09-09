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
    
    # Delete the reservation
    c.execute("DELETE FROM reservations WHERE id=?", (res_id,))
    
    # Renumber all IDs to be sequential
    c.execute("""
        UPDATE reservations 
        SET id = (
            SELECT COUNT(*) 
            FROM reservations r2 
            WHERE r2.rowid <= reservations.rowid
        )
    """)
    
    # Reset the auto-increment counter
    c.execute("UPDATE SQLITE_SEQUENCE SET seq = (SELECT MAX(id) FROM reservations) WHERE name='reservations'")
    
    conn.commit()
    conn.close()

def renumber_all_ids():
    """Utility function to renumber all reservation IDs"""
    conn = get_conn()
    c = conn.cursor()
    
    # Create a temporary table with sequential IDs
    c.execute("DROP TABLE IF EXISTS temp_reservations")
    c.execute("""
        CREATE TABLE temp_reservations AS 
        SELECT ROW_NUMBER() OVER (ORDER BY id) as new_id, 
               passenger_name, flight_number, date, seat, destination, ticket_class
        FROM reservations
    """)
    
    # Clear original table
    c.execute("DELETE FROM reservations")
    
    # Insert back with new sequential IDs
    c.execute("""
        INSERT INTO reservations (id, passenger_name, flight_number, date, seat, destination, ticket_class)
        SELECT new_id, passenger_name, flight_number, date, seat, destination, ticket_class
        FROM temp_reservations
    """)
    
    # Clean up
    c.execute("DROP TABLE temp_reservations")
    
    # Reset auto-increment
    c.execute("UPDATE SQLITE_SEQUENCE SET seq = (SELECT MAX(id) FROM reservations) WHERE name='reservations'")
    
    conn.commit()
    conn.close()