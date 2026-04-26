import sqlite3

def get_db_connection():
    conn = sqlite3.connect("database/lichens.db")
    conn.row_factory = sqlite3.Row
    return conn


def get_or_create_user(username):
    conn = sqlite3.connect("database/lichens.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT userID
        FROM users
        WHERE username = ?
    """, (username,))

    user = cursor.fetchone()

    if user is not None:
        conn.close()
        return user[0]

    cursor.execute("""
        INSERT INTO users (username)
        VALUES (?)
    """, (username,))

    conn.commit()
    new_user_id = cursor.lastrowid
    conn.close()

    return new_user_id




def get_all_lichens():
    conn = sqlite3.connect("database/lichens.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT l.id, l.name, l.comment, l.location, l.latitude, l.longitude,
               u.userID, u.username
        FROM lichens l
        LEFT JOIN users u
            ON l.userID = u.userID
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
            "longitude": row[5],
            "userID": row[6],
            "username": row[7]
        })

    return lichens


def get_lichen_by_id(id):
    conn = get_db_connection()
    lichen = conn.execute("SELECT * FROM lichens WHERE id = ?", (id,)).fetchone()
    conn.close()
    return lichen


def create_lichen(name, comment, location, latitude, longitude, user_id):
    conn = sqlite3.connect("database/lichens.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO lichens (name, comment, location, latitude, longitude, userID)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, comment, location, latitude, longitude, user_id))

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