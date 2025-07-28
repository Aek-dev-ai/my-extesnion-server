from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='public')

# تخدم صفحة الإضافة عند الدخول للرابط /
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'extension.html')

# تخدم أي ملف داخل مجلد public مثل zip أو صور
@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory(app.static_folder, filename)
