#code got from chatGPT - creating fucntion to connect flask commands to db

import sqlite3

def get_db_connection():
    conn = sqlite3.connect("database/lichens.db")
    conn.row_factory = sqlite3.Row
    return conn

from flask import Flask, request, jsonify
# code from chatgpt - setting up database - creating a table
# this will not be permanent - will delete this later

def init_db():
    conn = sqlite3.connect("database/lichens.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS lichens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT
    )
    """)

    conn.commit()
    conn.close()


app = Flask(__name__)

#@app.route("/")
#def home():
 #   return render_template("index.html")


@app.route('/lichens', methods=['GET'])
def getall():
    return "get all"

@app.route("/lichens", methods=["GET"])
def get_lichens():
    conn = get_db_connection()
    lichens = conn.execute("SELECT * FROM lichens").fetchall()
    conn.close()

    return str([dict(row) for row in lichens])
'''
#Create
@app.route('/lichens', methods=['POST'])
def create():
    name = request.form["name"]
    description = request.form["description"]

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO lichens (name, description) VALUES (?, ?)",
        (name, description)
    )
    conn.commit()
    conn.close()

    return "Lichen added"
'''
@app.route("/lichens", methods=["POST"])
def create_lichen():
    data = request.get_json()

    name = data["name"]
    description = data["description"]

    conn = get_db_connection()
    cursor = conn.execute(
        "INSERT INTO lichens (name, description) VALUES (?, ?)",
        (name, description)
    )
    conn.commit()
    conn.close()

    return jsonify({
        "id": cursor.lastrowid,
        "name": name,
        "description": description
    }), 201

# Update    
@app.route('/lichens/<int:id>', methods=['PUT'])
def update():
    jsonstring = request.json
    return f"update {id} {jsonstring}"

#Delete
@app.route('/lichens/<int:id>', methods=['DELETE'])
def delete():
    jsonstring = request.json
    return f"delete {id} {jsonstring}"

if __name__ == "__main__":
    
    init_db()
    
    app.run(debug=True)




