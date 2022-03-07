#!C:\Users\tkazinoti\AppData\Local\Programs\Python\Python310\python.exe
from database import cursor, db
import mysql.connector
import cgi, sys

print("Content-Type: text/html\r\n\r\n")
print(sys.stdin.read())

form = cgi.FieldStorage()
try:
    cursor.execute(f"""
    
    INSERT INTO `iwa`.`users`
    (`username`,
    `password_hash`,
    `is_admin`)
    VALUES
    ('{form.getvalue('collection-name')}',
    'uhfiuh7irfhui',
    1);
    """)
    db.commit()
except mysql.connector.Error:
    print("Error")

cursor.execute("SELECT * FROM users")
users = cursor.fetchall()
for user in users:
    print(user)

print('password hash: ', bytes(users[0][2]).decode('utf-8'))

with open('image.jpg', 'wb') as file:
    file.write(form.getvalue('fimg'))
