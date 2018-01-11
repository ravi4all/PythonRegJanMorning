Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/PythonMorning/Day_2/01-ForLoop.py 
Value of i is 0
Value of i is 1
Value of i is 2
Value of i is 3
Value of i is 4
Value of i is 5
Value of i is 6
Value of i is 7
Value of i is 8
Value of i is 9
Loop Ends
Unknown Indentation
>>> import turtle
>>> turt = turtle.Pen()
>>> turt.forward(200)
>>> turt.left(90)
>>> turt.forward(200)
>>> turt.left(90)
>>> turt.forward(200)
>>> turt.left(90)
>>> turt.forward(200)
>>> turt.left(90)
>>> turtle.reset()
>>> turt.reset()
>>> for i in range(0,5):
	turt.forward(200)
	turt.left(90)

	
>>> turt.reset()
>>> for i in range(0,4):
	turt.forward(200)
	turt.left(90)

	
>>> turt.reset()
>>> for i in range(0,30):
	turt.forward(3*i)
	turt.left(10*i)

	
>>> turt.reset()
>>> for i in range(0,30):
	turt.circle(10*i)

	
Traceback (most recent call last):
  File "<pyshell#25>", line 2, in <module>
    turt.circle(10*i)
  File "C:\Python36\lib\turtle.py", line 1990, in circle
    self.speed(speed)
  File "C:\Python36\lib\turtle.py", line 2174, in speed
    self.pen(speed=speed)
  File "C:\Python36\lib\turtle.py", line 2459, in pen
    self._update()
  File "C:\Python36\lib\turtle.py", line 2662, in _update
    screen._update()                  # TurtleScreenBase
  File "C:\Python36\lib\turtle.py", line 562, in _update
    self.cv.update()
  File "C:\Python36\lib\tkinter\__init__.py", line 1171, in update
    self.tk.call('update')
KeyboardInterrupt
>>> turt.reset()
>>> for i in range(0,30):
	turt.circle(6*i)
	turt.left(45)

	
Traceback (most recent call last):
  File "<pyshell#30>", line 2, in <module>
    turt.circle(6*i)
  File "C:\Python36\lib\turtle.py", line 1990, in circle
    self.speed(speed)
  File "C:\Python36\lib\turtle.py", line 2174, in speed
    self.pen(speed=speed)
  File "C:\Python36\lib\turtle.py", line 2459, in pen
    self._update()
  File "C:\Python36\lib\turtle.py", line 2662, in _update
    screen._update()                  # TurtleScreenBase
  File "C:\Python36\lib\turtle.py", line 562, in _update
    self.cv.update()
  File "C:\Python36\lib\tkinter\__init__.py", line 1171, in update
    self.tk.call('update')
KeyboardInterrupt
>>> turt.reset()
>>> turt.speed(0)
>>> for i in range(0,60):
	turt.circle(3*i)
	turt.left(45)

	
>>> 
