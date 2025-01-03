from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/node": {"origins": "*"}, r"/edge": {"origins": "*"}})  # Allow all origins for `/node` and `/edge`

# In-memory storage for nodes and edges (you can use a database instead)
nodes = []
edges = []

@app.route('/node', methods=['POST'])
def add_node():
    data = request.json
    node = {
        "_id": str(len(nodes) + 1),
        "name": data.get('name'),
        "type": data.get('type')
    }
    nodes.append(node)
    return jsonify({"message": "Node added successfully", "node": node}), 201

@app.route('/edge', methods=['POST'])
def add_edge():
    data = request.json
    edge = {
        "source": data.get('source'),
        "target": data.get('target'),
        "type": data.get('type')
    }
    edges.append(edge)
    return jsonify({"message": "Edge added successfully", "edge": edge}), 201

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
