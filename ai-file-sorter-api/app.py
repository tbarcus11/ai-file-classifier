from flask import Flask, send_from_directory
from routes.upload import upload_bp
import os

app = Flask(__name__)

# Register API routes
app.register_blueprint(upload_bp, url_prefix="/api")

# Serve frontend files
@app.route("/")
def index():
    return send_from_directory("frontend", "index.html")

@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory("frontend", path)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5005)
