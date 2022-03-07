#!C:\Users\tkazinoti\AppData\Local\Programs\Python\Python310\python.exe
import os
print("Content-Type: text/html\r\n\r\n")
print(os.getenv('QUERY_STRING'))

print("""
<form id="add-image-form" method="POST" action="./post.py" enctype="multipart/form-data">
    <select id="collection" name="collection">
        <option value="" selected disabled hidden>Choose collection</option>
        <option value="1">cards</option>
        <option value="2">cars</option>
        <option value="3">celebrities</option>
        <option value="4">animals</option>
        <option value="5">tech</option>
    </select>
    Selected: <span id="selected-collection"></span>
    
    <label for="collection-name">New collection: </label>
    <input type="text" name="collection-name" id="collection-name">
    
    <label for="fimg">Slika: </label>
    <input type="file" name="fimg" id="fimg">
    
    <input type="submit" value="OK">
</form>



""")