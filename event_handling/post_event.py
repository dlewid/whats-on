import json
import psycopg2
# from psycopg2 import sql, OperationalError



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


connection = psycopg2.connect(**db_params)

cursor = connection.cursor()

cursor.execute("Select * from events;")
db_version = cursor.fetchone()
print("Connected to database, version:", db_version)

cursor.close()
connection.close()


