import sqlite3

def get_db_connection():
    conn = sqlite3.connect("lichens.db")
    conn.row_factory = sqlite3.Row
    return conn


def get_all_lichens():
    conn = get_db_connection()
    lichens = conn.execute("SELECT * FROM lichens").fetchall()
    conn.close()
    return lichens


def get_lichen_by_id(id):
    conn = get_db_connection()
    lichen = conn.execute("SELECT * FROM lichens WHERE id = ?", (id,)).fetchone()
    conn.close()
    return lichen


def create_lichen(name, description):
    conn = get_db_connection()
    cursor = conn.execute(
        "INSERT INTO lichens (name, description) VALUES (?, ?)",
        (name, description)
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id


def update_lichen(id, name, description):
    conn = get_db_connection()
    conn.execute(
        "UPDATE lichens SET name = ?, description = ? WHERE id = ?",
        (name, description, id)
    )
    conn.commit()
    conn.close()


def delete_lichen(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM lichens WHERE id = ?", (id,))
    conn.commit()
    conn.close()