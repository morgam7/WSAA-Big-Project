import sqlite3
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "lichen_tracker.db")


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# -------------------------
# User functions
# -------------------------

def get_all_users():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT userID, username
        FROM users
        ORDER BY username
    """)

    rows = cursor.fetchall()

    users = []
    for row in rows:
        users.append({
            "userID": row["userID"],
            "username": row["username"]
        })

    conn.close()
    return users


def get_or_create_user(username):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT userID
        FROM users
        WHERE username = ?
    """, (username,))

    user = cursor.fetchone()

    if user is not None:
        user_id = user["userID"]
        conn.close()
        return user_id

    cursor.execute("""
        INSERT INTO users (username)
        VALUES (?)
    """, (username,))

    conn.commit()

    user_id = cursor.lastrowid

    conn.close()
    return user_id


# -------------------------
# Lichen functions
# -------------------------

def get_all_lichens():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            lichens.id,
            lichens.name,
            lichens.comment,
            lichens.location,
            lichens.latitude,
            lichens.longitude,
            lichens.userID,
            users.username
        FROM lichens
        LEFT JOIN users ON lichens.userID = users.userID
        ORDER BY lichens.id DESC
    """)

    rows = cursor.fetchall()

    lichens = []
    for row in rows:
        lichens.append({
            "id": row["id"],
            "name": row["name"],
            "comment": row["comment"],
            "location": row["location"],
            "latitude": row["latitude"],
            "longitude": row["longitude"],
            "userID": row["userID"],
            "username": row["username"]
        })

    conn.close()
    return lichens


def get_lichen_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            lichens.id,
            lichens.name,
            lichens.comment,
            lichens.location,
            lichens.latitude,
            lichens.longitude,
            lichens.userID,
            users.username
        FROM lichens
        LEFT JOIN users ON lichens.userID = users.userID
        WHERE lichens.id = ?
    """, (id,))

    lichen = cursor.fetchone()

    conn.close()
    return lichen


def create_lichen(name, comment, location, latitude, longitude, user_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO lichens 
        (name, comment, location, latitude, longitude, userID)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, comment, location, latitude, longitude, user_id))

    conn.commit()

    new_id = cursor.lastrowid

    conn.close()
    return new_id


def update_lichen(id, name, comment, location, latitude, longitude):
    conn = get_db_connection()
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
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM lichens
        WHERE id = ?
    """, (id,))

    conn.commit()
    conn.close()