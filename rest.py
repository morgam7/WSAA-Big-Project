from flask import Flask, request, jsonify, send_from_directory
import dao

app = Flask(__name__)


# -------------------------
# Page routes
# -------------------------

# -------------------------
# Page routes
# -------------------------

@app.route("/")
def login_page():
    """Landing page where the user selects or creates a username."""
    return send_from_directory("static", "login.html")


@app.route("/post")
def post_lichen_page():
    """Main page for submitting a new lichen record."""
    return send_from_directory("static", "index.html")


@app.route("/view")
def view_page():
    """Page for viewing all submitted lichen records."""
    return send_from_directory("static", "view.html")


@app.route("/update")
def update_page():
    """Page for updating an existing lichen record."""
    return send_from_directory("static", "update.html")


@app.route("/lichen")
def lichen_detail_page():
    """Page for viewing one lichen record in more detail."""
    return send_from_directory("static", "lichen.html")


@app.route("/lichen-name")
def lichen_name_page():
    """Page for searching or viewing lichens by name."""
    return send_from_directory("static", "lichen_name.html")


@app.route("/location")
def location_page():
    """Page for viewing lichens by location."""
    return send_from_directory("static", "location.html")


@app.route("/user")
def user_profile_page():
    """Profile-style page showing lichens posted by a user."""
    return send_from_directory("static", "user.html")


# -------------------------
# User API routes
# -------------------------

@app.route("/users", methods=["GET"])
def get_users():
    users = dao.get_all_users()
    return jsonify(users)


@app.route("/login", methods=["POST"])
def login_user():
    data = request.get_json() or {}
    username = data.get("username", "").strip()

    if not username:
        return jsonify({"error": "No username entered"}), 400

    user_id = dao.get_or_create_user(username)

    return jsonify({
        "userID": user_id,
        "username": username
    })


# -------------------------
# Lichen API routes
# -------------------------

@app.route("/lichens", methods=["GET"])
def get_lichens():
    """Return all lichen records from the database."""
    lichens = dao.get_all_lichens()
    return jsonify(lichens)


@app.route("/lichens/<int:id>", methods=["GET"])
def get_lichen(id):
    """Return one lichen record by ID."""
    lichen = dao.get_lichen_by_id(id)

    # Return a 404 response if the requested lichen does not exist.
    if lichen is None:
        return jsonify({"error": "Lichen not found"}), 404

    return jsonify(dict(lichen))


@app.route("/lichens", methods=["POST"])
def create_lichen():
    """Create a new lichen record from JSON data."""
    data = request.get_json() or {}

    # These fields are required before a lichen record can be saved.
    required_fields = [
        "username",
        "name",
        "comment",
        "location",
        "latitude",
        "longitude"
    ]

    # Check whether any required fields are missing or left blank.
    missing_fields = [
        field for field in required_fields
        if field not in data or str(data[field]).strip() == ""
    ]

    if missing_fields:
        return jsonify({
            "error": "Missing required fields",
            "missingFields": missing_fields
        }), 400

    # Clean text fields before saving them to the database.
    username = data["username"].strip()
    name = data["name"].strip()
    comment = data["comment"].strip()
    location = data["location"].strip()
    latitude = data["latitude"]
    longitude = data["longitude"]

    # Each lichen record is linked to a user.
    # If the username does not already exist, a new user is created.
    user_id = dao.get_or_create_user(username)

    # Save the new lichen record and return the new database ID.
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
    """Update an existing lichen record by ID."""
    existing_lichen = dao.get_lichen_by_id(id)

    # The record must exist before it can be updated.
    if existing_lichen is None:
        return jsonify({"error": "Lichen not found"}), 404

    data = request.get_json() or {}

    required_fields = [
        "name",
        "comment",
        "location",
        "latitude",
        "longitude"
    ]

    # Make sure the update request contains all required fields.
    missing_fields = [
        field for field in required_fields
        if field not in data or str(data[field]).strip() == ""
    ]

    if missing_fields:
        return jsonify({
            "error": "Missing required fields",
            "missingFields": missing_fields
        }), 400

    # Clean text fields before updating the database.
    name = data["name"].strip()
    comment = data["comment"].strip()
    location = data["location"].strip()
    latitude = data["latitude"]
    longitude = data["longitude"]

    # Update the lichen record using the DAO function.
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
    """Delete a lichen record by ID."""
    existing_lichen = dao.get_lichen_by_id(id)

    # Do not attempt to delete a record that is not in the database.
    if existing_lichen is None:
        return jsonify({"error": "Lichen not found"}), 404

    dao.delete_lichen(id)
    return jsonify({"message": "Lichen deleted"})


if __name__ == "__main__":
    app.run(debug=True)