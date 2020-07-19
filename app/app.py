from flask import Flask, render_template, app
from flask import request


app = Flask(__name__, template_folder='Template', static_folder='static')


@app.route('/')
def home():
    return render_template('pages/home.html')


@app.route('/scratch')
def scratch():
    return render_template('pages/scratch.html')


@app.route('/save', methods=['POST'])
def index():
    if request.method == 'POST':
        filebuffer = request.files['textfile']
        feature = filebuffer.read()
    with open("config.properties", 'w') as sdfFile:
        sdfFile.write(feature.decode('utf-8'))

    return 'qwer'

if __name__ == '__main__':
    app.run("127.0.0.1", 5000, debug=True)