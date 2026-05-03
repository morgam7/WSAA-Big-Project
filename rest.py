from flask import Flask, request, jsonify, send_from_directory
import dao

app = Flask(__name__)


# -------------------------
# Page routes
# -------------------------

@app.route("/")
def home():
    return send_from_directory("static", "index.html")


@app.route("/view")
def view_page():
    return send_from_directory("static", "view.html")


@app.route("/update")
def update_page():
    return send_from_directory("static", "update.html")


@app.route("/lichen")
def lichen_detail_page():
    return send_from_directory("static", "lichen.html")


@app.route("/lichen-name")
def lichen_name_page():
    return send_from_directory("static", "lichen_name.html")


@app.route("/location")
def location_page():
    return send_from_directory("static", "location.html")

@app.route("/user")
def user_page():
    return send_from_directory("static", "user.html")

# -------------------------
# User routes
# -------------------------

@app.route("/users", methods=["GET"])
def get_users():
    users = dao.get_all_users()
    return jsonify(users)


@app.route("/login", methods=["POST"])
def login_user():
    data = request.get_json()

    username = data["username"]

    if username is None or username.strip() == "":
        return jsonify({"error": "No username entered"}), 400

    user_id = dao.get_or_create_user(username)

    return jsonify({
        "userID": user_id,
        "username": username
    })


# -------------------------
# Lichen routes
# -------------------------

@app.route("/lichens", methods=["GET"])
def get_lichens():
    lichens = dao.get_all_lichens()
    return jsonify(lichens)


@app.route("/lichens/<int:id>", methods=["GET"])
def get_lichen(id):
    lichen = dao.get_lichen_by_id(id)

    if lichen is None:
        return jsonify({"error": "Lichen not found"}), 404

    return jsonify(dict(lichen))


@app.route("/lichens", methods=["POST"])
def create_lichen():
    data = request.get_json()

    username = data["username"]
    name = data["name"]
    comment = data["comment"]
    location = data["location"]
    latitude = data["latitude"]
    longitude = data["longitude"]

    user_id = dao.get_or_create_user(username)

    new_id = dao.create_lichen(
        name,
        comment,
        location,
        latitude,
        longitude,
        user_id
    )

    return jsonify({
        "id": new_id,
        "name": name,
        "comment": comment,
        "location": location,
        "latitude": latitude,
        "longitude": longitude,
        "userID": user_id,
        "username": username
    }), 201


@app.route("/lichens/<int:id>", methods=["PUT"])
def update_lichen(id):
    data = request.get_json()

    name = data["name"]
    comment = data["comment"]
    location = data["location"]
    latitude = data["latitude"]
    longitude = data["longitude"]

    dao.update_lichen(id, name, comment, location, latitude, longitude)

    return jsonify({
        "id": id,
        "name": name,
        "comment": comment,
        "location": location,
        "latitude": latitude,
        "longitude": longitude
    })


@app.route("/lichens/<int:id>", methods=["DELETE"])
def delete_lichen(id):
    dao.delete_lichen(id)
    return jsonify({"message": "Lichen deleted"})


if __name__ == "__main__":
    app.run(debug=True)





