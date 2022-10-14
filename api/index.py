import requests
import flask
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app, resources=r'/*')

@app.route('/github/<path:ghpath>', methods=["GET", "POST"])
def github(ghpath):
    url = 'https://github.com/{}'.format(ghpath)
    params = {
        'client_id': flask.request.json['client_id'],
        'client_secret': flask.request.json['client_secret'],
        'code': flask.request.json['code']
    }
    headers = {
        'accept': 'application/json'
    }
    result = requests.post(url=url, params=params, headers=headers, verify=False)
    return result.json()
