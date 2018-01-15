Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for i in range(97,110):
	print(chr(i))

	
a
b
c
d
e
f
g
h
i
j
k
l
m
>>> ord('a')
97
>>> def add():
	print("Addition called...")

	
>>> bin(3)
'0b11'
>>> for i in range(65,91):
	print(chr(i), end=' ')

	
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
>>> for i,j in enumerate(range(65,91)):
	print(i, chr(j), end=' ')

	
0 A 1 B 2 C 3 D 4 E 5 F 6 G 7 H 8 I 9 J 10 K 11 L 12 M 13 N 14 O 15 P 16 Q 17 R 18 S 19 T 20 U 21 V 22 W 23 X 24 Y 25 Z 
>>> for i,j in enumerate(range(65,91)):
	print(i, chr(j))

	
0 A
1 B
2 C
3 D
4 E
5 F
6 G
7 H
8 I
9 J
10 K
11 L
12 M
13 N
14 O
15 P
16 Q
17 R
18 S
19 T
20 U
21 V
22 W
23 X
24 Y
25 Z
>>> add()
Addition called...
>>> add
<function add at 0x0000022D34E9D6A8>
>>> def add():
	x = 10
	y = 12
	print(x+y)

	
>>> add
<function add at 0x0000022D340F3E18>
>>> add()
22
>>> x = add()
22
>>> type(x)
<class 'NoneType'>
>>> def add():
	x = 10
	y = 12
	print(x+y)
	return

>>> add()
22
>>> x = add()
22
>>> type(x)
<class 'NoneType'>
>>> x
>>> x = None
>>> x
>>> x
>>> type(x)
<class 'NoneType'>
>>> def add():
	global x
	x = 10
	y = 12
	print(x+y)

	
>>> x
>>> add()
22
>>> x
10
>>> def add():
	x = 10
	y = 12
	return x+y

>>> add()
22
>>> i = add()
>>> type(i)
<class 'int'>
>>> i
22
>>> def add():
	x = 10
	y = 12
	print(x+y)
	return x+y

>>> i = add()
22
>>> i
22
>>> def add(x,y):
	print(x+y)
	return x+y

>>> add(5,7)
12
12
>>> def add(x,y):
	print(x+y)

	
>>> add(5,7)
12
>>> print(add(5,7))
12
None
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/PythonMorning/Day_4/FunctionsBasics.py 
12
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/PythonMorning/Day_4/FunctionsBasics.py 
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/PythonMorning/Day_4/FunctionsBasics.py 
12
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/PythonMorning/Day_4/FunctionsBasics.py 
12
None
>>> 
