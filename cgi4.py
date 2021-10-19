#!/usr/bin/python37all
import cgi
import json

data = cgi.FieldStorage()

#json code
b1 = data.getvalue('option')
s1 = data.getvalue('slider1')
data = {"option":b1,"slider1":s1}
with open('lab4.txt', 'w') as f:
  json.dump(data,f)

print('Content-type: text/html\n\n')
print('''
<html>
<form action="/cgi-bin/cgi4.py" method="POST">
  <input type="radio" name="option" value="1" checked> LED 1 <br>
  <input type="radio" name="option" value="2"> LED 2 <br>
  <input type="radio" name="option" value="3"> LED 3 <br>
  <input type="submit" value="Submit">
''')
print('<input type="range" name="slider1" min="0" max="100" value="%s"><br>' % s1)
print('<input type="submit" value=”Change LED brightness">')
print('</form>')
print('Brightness = %s' % s1)
print('</html>')
