from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def exercises():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'exercises'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM exerciselist')
    results = [{exercise} for (exercise) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index():
    return str(exercises())

if __name__ == "__main__":
    app.run(port=80,host='0.0.0.0')