import sqlite3

def get_db_connection():
    conn = sqlite3.connect("database/lichens.db")
    conn.row_factory = sqlite3.Row
    return conn



def get_all_lichens():
    conn = sqlite3.connect("database/lichens.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, comment, location, latitude, longitude
        FROM lichens
    """)

    rows = cursor.fetchall()
    conn.close()

    lichens = []

    for row in rows:
        lichens.append({
            "id": row[0],
            "name": row[1],
            "comment": row[2],
            "location": row[3],
            "latitude": row[4],
            "longitude": row[5]
        })

    return lichens


def get_lichen_by_id(id):
    conn = get_db_connection()
    lichen = conn.execute("SELECT * FROM lichens WHERE id = ?", (id,)).fetchone()
    conn.close()
    return lichen


def create_lichen(name, comment, location, latitude, longitude):
    conn = sqlite3.connect("database/lichens.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO lichens (name, comment, location, latitude, longitude)
        VALUES (?, ?, ?, ?, ?)
    """, (name, comment, location, latitude, longitude))

    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return new_id


def update_lichen(id, name, comment, location, latitude, longitude):
    conn = sqlite3.connect("database/lichens.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE lichens
        SET name = ?, comment = ?, location = ?, latitude = ?, longitude = ?
        WHERE id = ?
    """, (name, comment, location, latitude, longitude, id))

    conn.commit()
    conn.close()


def delete_lichen(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM lichens WHERE id = ?", (id,))
    conn.commit()
    conn.close()