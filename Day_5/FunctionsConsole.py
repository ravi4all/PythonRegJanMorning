Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> eval('11+12')
23
>>> eval('11-12')
-1
>>> eval('11/12')
0.9166666666666666
>>> eval('11*12')
132
>>> eval('11%12')
11
>>> eval('12**2')
144
>>> x = {"1" : "+", "2" : "-"}
>>> x.get("1")
'+'
>>> x.get("2")
'-'
>>> opr = x.get("2")
>>> int(opr)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    int(opr)
ValueError: invalid literal for int() with base 10: '-'
>>> def outer():
	print("Outer function")
	def inner():
		print("Inner function")
	return inner

>>> outer()
Outer function
<function outer.<locals>.inner at 0x0000020E3E0249D8>
>>> outer()()
Outer function
Inner function
>>> inner = outer()
Outer function
>>> type(inner)
<class 'function'>
>>> inner90
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    inner90
NameError: name 'inner90' is not defined
>>> inner()
Inner function
>>> def outer():
	x = 10
	y = 12
	result = x + y
	def inner():
		print("This is inner")
	return inner, result

>>> outer()
(<function outer.<locals>.inner at 0x0000020E3E024950>, 22)
>>> x = outer()
>>> type(x)
<class 'tuple'>
>>> x,y = outer()
>>> x
<function outer.<locals>.inner at 0x0000020E3E024950>
>>> x()
This is inner
>>> y
22
>>> lambda x,y : x + y
<function <lambda> at 0x0000020E3E024B70>
>>> x = 10
>>> y = 12
>>> lambda x,y : x + y
<function <lambda> at 0x0000020E3E024950>
>>> 
>>> a = lambda x,y : x + y
>>> a(1,2)
3
>>> def calc(x,y):
	return x + y, x - y, x/y, x*y

>>> a,b,c,d = calc(10,13)
>>> a
23
>>> v
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    v
NameError: name 'v' is not defined
>>> b
-3
>>> c
0.7692307692307693
>>> d
130
>>> a,b = calc(10,12)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a,b = calc(10,12)
ValueError: too many values to unpack (expected 2)
>>> a,*b = calc(10,12)
>>> a
22
>>> b
[-2, 0.8333333333333334, 120]
>>> 
