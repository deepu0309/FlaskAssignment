from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_students():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)   # read file
        return jsonify(data)         # return JSON response
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format"}), 500


if __name__ == '__main__':
    app.run(debug=True)
