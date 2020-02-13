from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'this is a Flask'


@app.route('/dronks', methods=['GET', 'POST'])
def dronks():
    if request.method == 'POST':
        return request.json


if __name__ == "__main__":
    app.run()
