import flask
from flask import request, jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = False
# Create some test data for our catalog in the form of a list of dictionaries.
models = [
    {
        "id": 1,
        "model_name":"HPP001",
        "type":"PyTorch",
        "status":"approved",
        "stage":"production",
    },
    {
        "id": 2,
        "model_name":"HPP002",
        "type":"PyTorch",
        "status":"approved",
        "stage":"staging",
    }
]
@app.route('/', methods=['GET'])
def home():
    return '''<h1>VLib - Online Model Catalog</h1>
                <p>A flask api implementation for saving ML model information. </p>'''

@app.route('/api/models/all', methods=['GET'])
def api_all():
    return jsonify(models)
    
@app.route('/api/models', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        results = []
        return "Error: No id field provided. Please specify an id."
    for model in models:
        if model['id'] == id:
            results.append(model)
            return jsonify(results)

@app.route("/api/models",  methods = ['POST'])
def api_insert():
    model = request.get_json()
    models.append(model)
    return "Success: Model information has been added."

@app.route("/api/models/<id>", methods=["DELETE"])
def api_delete(id):
    for model in models:
        if model['id'] == int(id):
            models.remove(model)
    return "Success: Model information has been deleted."
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
