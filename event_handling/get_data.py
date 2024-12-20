import requests
from datetime import datetime, timezone
import json


# Could make a lot of accounts and change the static api_key to dependent on the object.
# This would be necessary if we needed a lot of accounts
class EventManager:
    # postgreSQL w3schools

    # Mapping of sports to API endpoints.
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


    def __init__(self, sport, today_date=None, api_key=None):
        self.today_date = self.parse_date(today_date)
        self.sport = sport.lower()
        self.api_key = api_key or self.fetch_api_key()     
        self.event_list = []
        self.games_today = self.sports_games_today()

    
    def parse_date(self, today_date):
        if isinstance(today_date, str):
            return datetime.fromisoformat(today_date).date()
        return datetime.now(timezone.utc).date()


    def fetch_api_key(self):
        try:
            with open('api_key.json', 'r') as file:
                data = json.load(file)
            return data.get(f"{self.sport}_api_key")
        except FileNotFoundError:
            raise FileNotFoundError("Api key file not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid Json format in API key file")


    def build_api_url(self):
        if self.sport not in self.sport_events:
            raise ValueError(f"Unsupported sports type")
        return f"https://api.sportsdata.io/v3/{self.sport}/scores/json/SchedulesBasic/2024"


    def fetch_games_data(self):
        url = self.build_api_url()
        try:
            response = requests.get(
                url, 
                headers={"Ocp-Apim-Subscription-Key": self.api_key},
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching data from API: {e}")
            return []


    def seperate_date_time(self, date_time):
        datetime_obj = datetime.fromisoformat(date_time)
        date = datetime_obj.date()
        time = datetime_obj.strftime("%I:%M %p")
        return (date, time)

    def sports_games_today(self):
        data = self.fetch_games_data()
        for game in data:
            game_date_str = game.get('Date')
            if game_date_str and isinstance(game_date_str, str):
                game_date = datetime.fromisoformat(game_date_str).date()
                if game_date == self.today_date:
                    date, time = self.seperate_date_time(game.get('DateTime'))
                    event = Event(
                        self.sport,
                        game.get('HomeTeam'),
                        game.get('AwayTeam'),
                        time,
                        game.get('GameID'),
                        date,
                    )
                    self.event_list.append(event)

    
    def print_events(self):
        for event in self.event_list:
            print(event)
    

# event class
class Event:
    def __init__(self, sport, home_team, away_team, event_time, game_id, event_date):
        self.sport = sport
        self.home_team = home_team
        self.away_team = away_team
        self.event_time = event_time
        self.game_id = game_id
        self.event_date = event_date
    

    def __str__(self):
        return (
            f"Sport: {self.sport}\n"
            f"Home Team: {self.home_team}\n"
            f"Away Team: {self.away_team}\n"
            f"Event Time (ET): {self.event_time}\n"
            f"Event Date: {self.event_date}\n"
            f"Game ID: {self.game_id}\n"
        )


# test
find_events = EventManager("nfl", "2024-11-03")
find_events.print_events()
