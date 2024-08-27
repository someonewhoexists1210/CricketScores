import flask, requests, json, os
from flask import request, jsonify
from dotenv import load_dotenv

app = flask.Flask(__name__)

load_dotenv()
API_KEY = os.getenv('API_KEY')

@app.route('/', methods=['GET'])
def home():
    response = requests.get(f'https://api.cricapi.com/v1/currentMatches?apikey={API_KEY}&offset=0')
    if response.status_code == 200:
        result = response.json()
        data = result['data']
        tosend = []
        for i in data:
            if i['matchStarted'] and not i['matchEnded']:
                tosend.append(i)

        return jsonify(tosend)

if __name__ == '__main__':
    app.run(debug=True)