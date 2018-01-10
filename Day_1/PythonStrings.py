Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> name = "Ravi Tyagi"
>>> name[0]
'R'
>>> name[3]
'i'
>>> name[0:]
'Ravi Tyagi'
>>> name[0:5]
'Ravi '
>>> name[:5]
'Ravi '
>>> name[1:4]
'avi'
>>> name[0] = 'K'
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    name[0] = 'K'
TypeError: 'str' object does not support item assignment
>>> name.replace('R', 'K')
'Kavi Tyagi'
>>> name
'Ravi Tyagi'
>>> name[-1]
'i'
>>> name[0:-1]
'Ravi Tyag'
>>> name[0:6:2]
'Rv '
>>> name[0:9:2]
'Rv yg'
>>> name[::-1]
'igayT ivaR'
>>> name == name[::-1]
False
>>> a = 10
>>> b = a
>>> a is b
True
>>> b = 11
>>> a is b
False
>>> name is name[::-1]
False
>>> a = [1,2,3,4,5]
>>> b = [1,2,3,4,5]
>>> a == b
True
>>> a is b
False
>>> type(a)
<class 'list'>
>>> a = [1,2,3,4,5,'Hi','Hello',10.5,True]
>>> name = 'ravi tyagi'
>>> name.upper()
'RAVI TYAGI'
>>> name.capitalize()
'Ravi tyagi'
>>> name.find('a')
1
>>> name.rfind('a')
7
>>> name.count('i')
2
>>> name.isdecimal()
False
>>> 
