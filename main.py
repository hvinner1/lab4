!/usr/bin/python37all
#Save file as /usr/lib/cgi-bin/testS.py

print('''
<html>
<form action="/cgi-bin/radio.py" method="POST">
  <input type="radio" name="option" value="1" checked> LED 1 <br>
  <input type="radio" name="option" value="2"> LED 2 <br>
  <input type="radio" name="option" value="3"> LED 3 <br>
  <input type="submit" value="Submit">
</form>
</html>

<html>
<form action="/cgi-bin/led_pwm.py" method="POST">
<input type="range" name="slider1" min ="0" max="100" value ="0"><br>
<input type="submit" value=”Change LED brightness">
</form>
</html>
''')