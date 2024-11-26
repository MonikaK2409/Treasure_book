from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import os
#from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes
#CORS(app)

# MongoDB connection setup
mongo_host = os.getenv('MONGO_HOST', 'mongodb')  # MongoDB container hostname
client = MongoClient(f"mongodb://{mongo_host}:27017/")  # MongoDB connection string
db = client['treasurebook']

@app.route('/')
def home():
    return render_template('index.html')  # Ensure 'index.html' is in the templates folder

@app.route('/node', methods=['POST'])
def add_node():
    try:
        data = request.json
        if not data or not data.get('name') or not data.get('type'):
            return jsonify({"error": "Invalid input, 'name' and 'type' are required"}), 400

        # Insert the node into the 'nodes' collection in MongoDB
        node = {
            'name': data.get('name'),
            'type': data.get('type')
        }
        inserted_node = db.nodes.insert_one(node)
        
        # Convert the ObjectId to a string for serialization
        node['_id'] = str(inserted_node.inserted_id)
        
        return jsonify({"message": "Node added successfully", "node": node}), 201
    except Exception as e:
        return jsonify({"error": f"Error: {str(e)}"}), 500

@app.route('/edge', methods=['POST'])
def add_edge():
    try:
        data = request.json
        if not data or not data.get('source') or not data.get('target') or not data.get('type'):
            return jsonify({"error": "Invalid input, 'source', 'target', and 'type' are required"}), 400

        # Insert the edge into the 'edges' collection in MongoDB
        edge = {
            'source': data.get('source'),
            'target': data.get('target'),
            'type': data.get('type')
        }
        inserted_edge = db.edges.insert_one(edge)

        # Convert the ObjectId to a string for serialization
        edge['_id'] = str(inserted_edge.inserted_id)

        return jsonify({"message": "Edge added successfully", "edge": edge}), 201
    except Exception as e:
        return jsonify({"error": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Enable debug mode for more insights
