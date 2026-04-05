from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_status', methods=['POST'])
def fetch_status():
    uid = request.json.get('uid')
    if not uid:
        return jsonify({"error": "UID required"}), 400
    
    # Timro API Link
    api_url = f"https://player-status-ff-gf.onrender.com/s?uid={uid}"
    
    try:
        # API bata data tanne
        response = requests.get(api_url, timeout=10)
        # API le text response dincha bhane teslai logically pathaune
        return jsonify({"success": True, "data": response.text})
    except Exception as e:
        return jsonify({"success": False, "error": "Connection Timeout"}), 500

if __name__ == '__main__':
    app.run(debug=True)
