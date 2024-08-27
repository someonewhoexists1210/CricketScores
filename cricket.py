import flask, requests, json, os
from flask import request, jsonify, render_template
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

        return render_template('index.html', data=tosend)

@app.route('/player', methods=['GET'])
def player_stats():
    id = 0
    player = request.args.get('name')
    if player:
        response = requests.get(f'https://api.cricapi.com/v1/players?apikey={API_KEY}&search={player}')
        if response.status_code == 200:
            result = response.json()
            id = result['data'][0]['id']
    if id:
        response = requests.get(f'https://api.cricapi.com/v1/players_info?apikey={API_KEY}&offset=0&id={id}')
        if response.status_code == 200:
            result = response.json()
            return render_template('player.html', player=result['data'])
        
    return jsonify({'error': 'Player not found'})


            
if __name__ == '__main__':
    app.run(debug=True)