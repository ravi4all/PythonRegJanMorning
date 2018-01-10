Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("Hello")
Hello
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/PythonMorning/PythonBasics.py 
22
>>> num_1
10
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/PythonMorning/PythonBasics.py 
22
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/PythonMorning/PythonBasics.py 
Traceback (most recent call last):
  File "C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/PythonMorning/PythonBasics.py", line 7, in <module>
    print("Sum is"+result)
TypeError: must be str, not int
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/PythonMorning/PythonBasics.py 
Sum is 22
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/PythonMorning/PythonBasics.py 
Sum is22
>>> a = 10
>>> str(a)
'10'
>>> float(a)
10.0
>>> int(a)
10
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/PythonMorning/PythonBasics.py 
Sum is 10 and 12 is 22
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/PythonMorning/PythonBasics.py 
Sum of 10 and 12 is 22
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/PythonMorning/PythonBasics.py 
Sum of 10 and 12 is 22
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/PythonMorning/PythonBasics.py 
Sum of 10 and 12 is 22
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/PythonMorning/PythonBasics.py 
Sum of 10.000000 and 12.000000 is 22.000000
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/PythonMorning/PythonInput.py 
Enter first number : 2
Enter second number : 2
Sum is 22
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/PythonMorning/PythonInput.py 
Enter first number : 12
Enter second number : 12
Sum is 1212
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/PythonMorning/PythonInput.py 
Enter first number : 12
Enter second number : 11
Sum is 23
>>> a = 12
>>> id(a)
1916586000
>>> id(12)
1916586000
>>> b = a
>>> id(b)
1916586000
>>> a = 12
>>> a = 10
>>> id(a)
1916585936
>>> id(10)
1916585936
>>> del b
>>> import sys
>>> sys.getsizeof(a)
28
>>> a = 123123123213123123123123123213123
>>> sys.getsizeof(a)
40
>>> x = "Hello"
>>> sys.getsizeof(x)
54
>>> 
