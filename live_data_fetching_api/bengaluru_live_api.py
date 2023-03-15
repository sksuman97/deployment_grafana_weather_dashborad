import random
import requests
import psycopg2
import requests
import time
from datetime import datetime
import pytz

# Define timescaleDB server details
db_host = 'temperature_db'
db_port = 5432
db_name = 'mydb'
db_user = 'postgres'
db_password = 'postgres'


# Define city and API key
city = 'Bengaluru'
api_key = '92892253a52263470cd52ae6c4386424'

# Define API endpoint to fetch temperature data
api_url = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

# Specifying location for timezone
IST = pytz.timezone('Asia/Kolkata')


# Connect to the database
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
)

# Create a cursor object
cur = conn.cursor()

# Main loop
while True:
    # Fetch temperature data from the API
    response = requests.get(api_url.format(city=city, api_key=api_key))
    temperature = response.json()['main']['temp']
    temperature_feels = response.json()['main']['feels_like']
    pressure = response.json()['main']['pressure']
    humidity = response.json()['main']['humidity']
    # Wind information
    wind_speed = response.json()['wind']['speed']
    wind_direction = response.json()['wind']['deg']
    # Visibility
    visibility = response.json()['visibility']
    # Cloudiness
    cloudiness = response.json()['clouds']['all']
    # Insert the temperature data into the database
    timestamp = datetime.now(IST).strftime('%Y-%m-%d %H:%M:%S.%f')
    cur.execute("INSERT INTO bengaluru_temperature (timestamp, temperature, temperature_feels, pressure, humidity, wind_speed, wind_direction, visibility, cloudiness) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (timestamp, temperature, temperature_feels, pressure, humidity, wind_speed, wind_direction, visibility, cloudiness))
    conn.commit()
    # Wait for one minute
    time.sleep(90)

# Close the database connection
cur.close()
conn.close()




