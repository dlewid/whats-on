import requests
from datetime import datetime, timezone
import json


# Could make a lot of accounts and change the static api_key to dependent on the object.
# This would be necessary if we needed a lot of accounts
class EventManager:
    # secret key
    # postgreSQL w3schools

    # all possible sports events but only nfl works right now 
    sport_events = {
        "nfl" : "nfl",
        "mlb" : "mlb",
        "nba" : "nba",
        "nhl" : "nhl",
        "college football" : "cfb",
        "college basketball" : "cbb",
        "golf" : "golf",
        "nascar" : "nascar",
        "soccer" : "soccer",
        "mma" : "mma",
        "wnba" : "wnba",
        "college womens basketball" : "cwbb",
        "tennis" : "tennis",
    }


    def __init__(self, sport, api_key=None, today_date=None):
        # Convert string date to datetime.date if provided as string
        if isinstance(today_date, str):
            self.today_date = datetime.fromisoformat(today_date).date()
        elif today_date is None:
            self.today_date = datetime.now(timezone.utc).date()
        else:
            self.today_date = today_date
        
        self.sport = sport.lower()
        self.api_key = self.fetch_api_key()     
        self.event_list = []
        self.games_today = self.sports_games_today()


    def fetch_api_key(self) -> json:
        with open('api_key.json', 'r') as file:
            data = json.load(file)
        return data.get(f"{self.sport}_api_key")


    def sports_games_today(self):
        url = f"https://api.sportsdata.io/v3/{self.sport}/scores/json/SchedulesBasic/2024"

        try:
            response = requests.get(
                url, 
                headers={"Ocp-Apim-Subscription-Key": self.api_key},
                timeout=10
            )

            response.raise_for_status()

            data = response.json()

            for game in data:
                game_date_str = game.get('Date')
                if game_date_str and isinstance(game_date_str, str):
                    game_date = datetime.fromisoformat(game_date_str).date()
                    if game_date == self.today_date:
                        event = Event(self.sport, game.get('HomeTeam'), game.get('AwayTeam'), game.get('DateTime'), game.get('GameID'))
                        self.event_list.append(event)

        except ValueError as e:
            return e
    
    def print_events(self):
        for event in self.event_list:
            print(event)
    

# event class
class Event (EventManager):
    def __init__(self, sport, home_team, away_team, event_time, game_id):
        self.sport = sport
        self.home_team = home_team
        self.away_team = away_team
        self.event_time = event_time
        self.game_id = game_id
    

    def __str__(self):
        return f"Sport: {self.sport}\nHome Team: {self.home_team}\nAway Team: {self.away_team}\nEvent Time: {self.event_time}\nGame ID: {self.game_id}\n"


# test
find_events = EventManager("nfl", "2024-09-05")
find_events.print_events()
