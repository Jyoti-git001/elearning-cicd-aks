from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"service": "elearning-frontend", "status": "running"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/courses')
def courses():
    return jsonify({"courses": ["Python Basics", "Azure DevOps", "Docker & Kubernetes"]})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
