from flask import Flask, send_from_directory, request, jsonify, session, abort
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__, static_folder='public')
CORS(app)
app.secret_key = 'super-secret-key'

# هيكل التوكنات مع تواريخ الانتهاء
VALID_TOKENS = {
    "abc123": "2025-06-30",
    "xyz456": "2025-09-01",
    "dzflako2025": "2025-12-31"
}

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'extension.html')

@app.route('/validate-token', methods=['POST'])
def validate_token():
    data = request.get_json()
    token = data.get('token', '')

    expiration = VALID_TOKENS.get(token)
    if expiration:
        now = datetime.now().date()
        exp_date = datetime.strptime(expiration, "%Y-%m-%d").date()
        if now <= exp_date:
            session['valid_token'] = True
            return jsonify({'status': 'ok'})
        else:
            return jsonify({'error': 'Token expired'}), 403
    else:
        return jsonify({'error': 'Invalid token'}), 403

@app.route('/download')
def download_extension():
    if session.get('valid_token'):
        return send_from_directory(app.static_folder, "App'Services.zip", as_attachment=True)
    else:
        abort(403)
