from flask import Flask, request


app = Flask(__name__)

@app.route("/")
def home():
    return "Lichen Tracker is running"

@app.route('/lichens', methods=['GET'])
def getall():
    return "get all"

@app.route('/lichens/<int:id>', methods=['GET'])
def findbyid(id):
    return "find by id"

#Create
@app.route('/lichens', methods=['POST'])
def create():
    #read in json from the body
    return "create"
    f"create {jsonstring}"

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
    app.run(debug=True)

