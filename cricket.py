import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def get_live_scores(team_name):
    url = 'https://www.espncricinfo.com/live-cricket-score'
    
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f'Failed to retrieve the page. Status code: {response.status_code}')
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    match_containers = soup.find_all('div', class_='cscore')

    live_matches = []
    last_match = None

    for match in match_containers:
        try:
            teams = match.find_all('a', class_='cscore_name cscore_name--long')
            scores = match.find_all('div', class_='cscore_score')

            if teams and scores:
                team1 = teams[0].text.strip()
                team2 = teams[1].text.strip()
                score1 = scores[0].text.strip()
                score2 = scores[1].text.strip()

                if team_name.lower() in team1.lower() or team_name.lower() in team2.lower():
                    live_matches.append({
                        'Team 1': team1,
                        'Score 1': score1,
                        'Team 2': team2,
                        'Score 2': score2,
                    })
        except Exception as e:
            print(f'Error extracting live match details: {e}')

    if not live_matches:
        try:
            last_match_container = soup.find('div', class_='cscore_info-overview')

            teams = last_match_container.find_all('a', class_='cscore_name cscore_name--long')
            scores = last_match_container.find_all('div', class_='cscore_score')

            if teams and scores:
                team1 = teams[0].text.strip()
                team2 = teams[1].text.strip()
                score1 = scores[0].text.strip()
                score2 = scores[1].text.strip()

                if team_name.lower() in team1.lower() or team_name.lower() in team2.lower():
                    last_match = {
                        'Team 1': team1,
                        'Score 1': score1,
                        'Team 2': team2,
                        'Score 2': score2,
                    }
        except Exception as e:
            print(f'Error extracting last match details: {e}')

    if live_matches:
        df = pd.DataFrame(live_matches)
        return df
    elif last_match:
        df = pd.DataFrame([last_match])
        return df
    else:
        print(f'No live or last match found for the team: {team_name}')
        return None

if __name__ == "__main__":
    team_name = input("Enter the team name to get live or last match scores: ")
    scores_df = get_live_scores(team_name)
    if scores_df is not None:
        print(scores_df)
