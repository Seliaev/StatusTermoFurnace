from flask import Flask, render_template
from Modbus.get_data import get_data_from_sp

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    data_dict = get_data_from_sp(test=True) # Удалить атрибут, при подключенном устройстве
    return render_template('index.html', data_dict=data_dict)


