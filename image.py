#!C:\Users\tkazinoti\AppData\Local\Programs\Python\Python310\python.exe
import cgi

print("Content-Type: text/html\r\n\r\n")

q = cgi.FieldStorage()

print(f"""

<h1>{q.getvalue('id')}</h1>

""")
