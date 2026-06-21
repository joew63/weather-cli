import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

def insert_weather(date, name, temp, feels_like, humidity, wind, description):
    cursor.execute('CREATE TABLE IF NOT EXISTS weather(date, name, temp, feels_like, humidity, wind, description)')
    cursor.execute(
        "INSERT INTO weather VALUES (?, ?, ?, ?, ?, ?, ?)",
        (date, name, temp, feels_like, humidity, wind, description)
    )
    connection.commit()

def get_rows():
    cursor.execute('SELECT * FROM weather')
    return cursor.fetchall()