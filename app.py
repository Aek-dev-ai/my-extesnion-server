# app.py
from flask import Flask, send_from_directory

app = Flask(name, static_folder="public")

@app.route("/")
def index():
    return "🧩 Chrome Extension Download Server"

@app.route("/my-extension.zip")
def download_extension():
    return send_from_directory("public", "my-extension.zip", as_attachment=True)