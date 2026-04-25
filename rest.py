#code got from chatGPT - creating fucntion to connect flask commands to db

from flask import Flask, request, jsonify, send_from_directory
import dao

app = Flask(__name__)

# Page routes
@app.route("/")
def home():
    return send_from_directory("static", "index.html")

@app.route("/view")
def view_page():
    return send_from_directory("static", "view.html")


@app.route("/update")
def update_page():
    return send_from_directory("static", "update.html")

'''
@app.route("/delete")
def delete_page():
    return send_from_directory("static", "delete.html")

'''



@app.route("/lichens", methods=["GET"])
def get_lichens():
    lichens = dao.get_all_lichens()
    return jsonify(lichens)




@app.route("/lichens/<int:id>", methods=["GET"])
def get_lichen(id):
    lichens = dao.get_lichen_by_id(id)
    if lichens is None:
        return jsonify({"error": "Lichen not found"}), 404
    return jsonify(dict(lichen))


@app.route("/lichens", methods=["POST"])
def create_lichen():
    data = request.get_json()

    name = data["name"]
    comment = data["comment"]
    location = data["location"]
    latitude = data["latitude"]
    longitude = data["longitude"]

    new_id = dao.create_lichen(name, comment, location, latitude, longitude)

    return jsonify({
        "id": new_id,
        "name": name,
        "comment": comment,
        "location": location,
        "latitude": latitude,
        "longitude": longitude
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





