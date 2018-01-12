Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tup = (1,2,3,4,5,'Hi','Hello',10.5)
>>> tup[4]
5
>>> tup[0:4]
(1, 2, 3, 4)
>>> sorted(tup)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    sorted(tup)
TypeError: '<' not supported between instances of 'str' and 'int'
>>> tup[0] = 'Bye'
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tup[0] = 'Bye'
TypeError: 'tuple' object does not support item assignment
>>> a = [1,2,3,4,5,6,7]
>>> tuple(a)
(1, 2, 3, 4, 5, 6, 7)
>>> 
