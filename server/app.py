from flask import Flask, render_template, jsonify
from Modbus.get_data import get_data_from_sp

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    data_dict = get_data_from_sp()
    return render_template('index.html', data_dict=data_dict)

@app.route('/get_data')
def get_data():
    data_dict = get_data_from_sp()
    return jsonify(data_dict)

