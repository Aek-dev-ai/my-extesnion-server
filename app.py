from flask import Flask, send_from_directory, request, jsonify, session, abort
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='public')
CORS(app)

# سر لجلسات المستخدم
app.secret_key = 'super-secret-key'

# قائمة التوكنات المسموحة (مثال)
VALID_TOKENS = {'abc123', 'xyz456', 'dzflako2025'}

# عرض صفحة HTML
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'extension.html')

# تحقق من التوكن
@app.route('/validate-token', methods=['POST'])
def validate_token():
    data = request.get_json()
    token = data.get('token', '')

    if token in VALID_TOKENS:
        # حفظ التوكن في الجلسة للسماح بالتحميل
        session['valid_token'] = True
        return jsonify({'status': 'ok'})
    else:
        return jsonify({'error': 'Invalid token'}), 403

# مسار التحميل بعد التحقق
@app.route('/download')
def download_extension():
    if session.get('valid_token'):
        return send_from_directory(app.static_folder, "App'Services.zip", as_attachment=True)
    else:
        abort(403)  # رفض التحميل بدون توكن
