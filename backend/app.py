from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"service": "elearning-backend", "status": "running"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/users')
def users():
    return jsonify({"users": [{"id": 1, "name": "Student A"}, {"id": 2, "name": "Student B"}]})

@app.route('/api/enrollments')
def enrollments():
    return jsonify({"enrollments": [{"user_id": 1, "course": "Azure DevOps"}]})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
