from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

dicfriend = {}
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    result = request.get_json()
    dicfriend[result['name']] = result['friends']

    print(dicfriend)
    return {'ok':'ok'}

@app.route('/wjadmin', methods=['POST'])
def admin():
    return{'friend':dicfriend}
