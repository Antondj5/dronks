import requests
from flask import Flask, request

app = Flask(__name__)

endpoint = "https://notify.run/2JjjVHr40X4IATHn"


@app.route('/')
def index():
    return 'this is a Flask'


@app.route('/dronks', methods=['GET', 'POST'])
def dronks():
    if request.method == 'POST':
        requests.post(endpoint,data=request.json)
        return request.json


if __name__ == "__main__":
    app.run()
