import json
import psycopg2
import get_data
# from psycopg2 import sql, OperationalError

# Setting up db parameters using 'db.json'.
try:
    with open('db.json', 'r') as file:
        data = json.load(file)
        db_params = {
            "host": data.get('endpoint'),
            "port": data.get('port'),
            "database": "events",
            "user": data.get('username'),
            "password": data.get('password')
        }
except FileNotFoundError:
    raise FileNotFoundError(f"{file} file not found")
except json.JSONDecodeError:
    raise ValueError(f"Invalid Json format in {file} file")

def post_data(sport):
    # Setting up the connection to the db.
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    events_manager = get_data.EventManager(sport)
    events = events_manager.event_list

    # Query for inserting event data into rows.
    for event in events:
        cursor.execute(
            """
            INSERT INTO events (event_id, home_team, away_team, sport, event_date, event_time)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (event.game_id, event.home_team, event.away_team, event.sport, event.event_date, event.event_time)
        )

    # Saving the data to the db.
    connection.commit()
    # Closing the connection to the db.
    cursor.close()
    connection.close()

post_data("nfl")



