#!C:\Users\tkazinoti\AppData\Local\Programs\Python\Python310\python.exe
import mysql.connector
import os
import cgitb
cgitb.enable()

USERNAME = 'root'
PASSWORD = os.getenv('SQL_PASSWORD', 'root')
HOST = 'localhost'
DB_NAME = 'iwa'

config = {
    'user': USERNAME,
    'password': '',
    'host': HOST,
    'database': 'iwa'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()
