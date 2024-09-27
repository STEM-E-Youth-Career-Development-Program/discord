import sqlite3

def loadData():
    database = sqlite3.connect('data.db')
    cursor = database.cursor()
    database.execute("CREATE TABLE IF NOT EXISTS user_data (user_id INT PRIMARY KEY, nickname VARCHAR(255), timezone VARCHAR(255) DEFAULT 'CST', birthday DATE, roles TEXT, points BIGINT)")