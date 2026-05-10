import os
import sqlite3


# Build the database path relative to this file.
# This means the app can still find the database when run from the project folder.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "lichen_tracker.db")


def get_db_connection():
    """Create and return a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)

    # This lets rows behave like dictionaries, e.g. row["username"].
    conn.row_factory = sqlite3.Row

    return conn


# -------------------------
# User database functions
# -------------------------

def get_all_users():
    """Return all users from the users table."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT userID, username
        FROM users
        ORDER BY username
    """)

    rows = cursor.fetchall()
    conn.close()

    # Convert SQLite rows into normal dictionaries for JSON responses.
    users = []
    for row in rows:
        users.append({
            "userID": row["userID"],
            "username": row["username"]
        })

    return users


def get_or_create_user(username):
    """
    Return the ID for an existing username.
    If the username does not already exist, create a new user first.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT userID
        FROM users
        WHERE username = ?
    """, (username,))

    user = cursor.fetchone()

    # If the user already exists, return their existing ID.
    if user is not None:
        user_id = user["userID"]
        conn.close()
        return user_id

    # Otherwise, insert a new user record.
    cursor.execute("""
        INSERT INTO users (username)
        VALUES (?)
    """, (username,))

    conn.commit()
    user_id = cursor.lastrowid

    conn.close()
    return user_id


# -------------------------
# Lichen database functions
# -------------------------

def get_all_lichens():
    """
    Return all lichen records.
    Each lichen is joined with the username of the person who submitted it.
    """
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
    conn.close()

    # Convert rows into dictionaries so Flask can return them as JSON.
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

    return lichens


def get_lichen_by_id(id):
    """Return one lichen record by ID, including the linked username."""
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
    """Insert a new lichen record and return its new database ID."""
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
    """Update an existing lichen record."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE lichens
        SET 
            name = ?, 
            comment = ?, 
            location = ?, 
            latitude = ?, 
            longitude = ?
        WHERE id = ?
    """, (name, comment, location, latitude, longitude, id))

    conn.commit()
    conn.close()


def delete_lichen(id):
    """Delete a lichen record from the database by ID."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM lichens
        WHERE id = ?
    """, (id,))

    conn.commit()
    conn.close()