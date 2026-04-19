#code got from chatGPT - creating fucntion to connect flask commands to db

from flask import Flask, request, jsonify
import dao

app = Flask(__name__)

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/lichens", methods=["GET"])
def get_lichens():
    lichens = dao.get_all_lichens()
    return jsonify([dict(row) for row in lichens])


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
    description = data["description"]

    new_id = dao.create_lichen(name, description)

    return jsonify({
        "id": new_id,
        "name": name,
        "description": description
    }), 201


@app.route("/lichens/<int:id>", methods=["PUT"])
def update_lichen(id):
    data = request.get_json()
    name = data["name"]
    description = data["description"]

    dao.update_lichen(id, name, description)

    return jsonify({
        "id": id,
        "name": name,
        "description": description
    })


@app.route("/lichens/<int:id>", methods=["DELETE"])
def delete_lichen(id):
    dao.delete_lichen(id)
    return jsonify({"message": "Lichen deleted"})

if __name__ == "__main__":
    app.run(debug=True)





