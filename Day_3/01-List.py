Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> arr = [1,2,3,'Hi',10.5]
>>> arr[0:5]
[1, 2, 3, 'Hi', 10.5]
>>> arr = []
>>> arr.append(100)
>>> arr
[100]
>>> arr.append(101)
>>> arr
[100, 101]
>>> arr.append(102)
>>> arr
[100, 101, 102]
>>> arr.append(103,104,105)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    arr.append(103,104,105)
TypeError: append() takes exactly one argument (3 given)
>>> arr.append([103,104,105])
>>> arr
[100, 101, 102, [103, 104, 105]]
>>> arr[-1]
[103, 104, 105]
>>> arr[-1][0]
103
>>> arr.append('Hello')
>>> arr.append(11.45)
>>> arr.append(99)
>>> arr
[100, 101, 102, [103, 104, 105], 'Hello', 11.45, 99]
>>> arr.pop()
99
>>> arr
[100, 101, 102, [103, 104, 105], 'Hello', 11.45]
>>> arr.insert(1,'Python')
>>> arr
[100, 'Python', 101, 102, [103, 104, 105], 'Hello', 11.45]
>>> arr.pop(1)
'Python'
>>> arr
[100, 101, 102, [103, 104, 105], 'Hello', 11.45]
>>> arr.index(11.45)
5
>>> arr.index(105)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    arr.index(105)
ValueError: 105 is not in list
>>> arr[3].append(106)
>>> arr
[100, 101, 102, [103, 104, 105, 106], 'Hello', 11.45]
>>> arr.remove('Hello')
>>> arr
[100, 101, 102, [103, 104, 105, 106], 11.45]
>>> arr.extend('Hello')
>>> arr
[100, 101, 102, [103, 104, 105, 106], 11.45, 'H', 'e', 'l', 'l', 'o']
>>> arr.extend(111)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    arr.extend(111)
TypeError: 'int' object is not iterable
>>> arr_2 = [111,112,113,114]
>>> arr.extend(arr_2)
>>> arr
[100, 101, 102, [103, 104, 105, 106], 11.45, 'H', 'e', 'l', 'l', 'o', 111, 112, 113, 114]
>>> arr
[100, 101, 102, [103, 104, 105, 106], 11.45, 'H', 'e', 'l', 'l', 'o', 111, 112, 113, 114]
>>> arr[3].pop()
106
>>> arr
[100, 101, 102, [103, 104, 105], 11.45, 'H', 'e', 'l', 'l', 'o', 111, 112, 113, 114]
>>> arr[3].pop(1)
104
>>> arr = [15,23,45,67,11,3,6,34,66]
>>> sorted(arr)
[3, 6, 11, 15, 23, 34, 45, 66, 67]
>>> sorted(arr, reverse = True)
[67, 66, 45, 34, 23, 15, 11, 6, 3]
>>> arr
[15, 23, 45, 67, 11, 3, 6, 34, 66]
>>> arr.sort()
>>> arr
[3, 6, 11, 15, 23, 34, 45, 66, 67]
>>> arr.sort(reverse=True)
>>> arr
[67, 66, 45, 34, 23, 15, 11, 6, 3]
>>> arr = sorted(arr)
>>> arr
[3, 6, 11, 15, 23, 34, 45, 66, 67]
>>> 45 in arr
True
>>> a = [1,2,3,4,5,6,7,8]
>>> import sys
>>> sys.getsizeof(a)
128
>>> a = []
>>> sys.getsizeof(a)
64
>>> a = [1,2,3,4,5,6,7,8]
>>> b = a
>>> id(b)
2399572778696
>>> id(a)
2399572778696
>>> a[0] = 'Hello'
>>> a
['Hello', 2, 3, 4, 5, 6, 7, 8]
>>> b
['Hello', 2, 3, 4, 5, 6, 7, 8]
>>> a[:]
['Hello', 2, 3, 4, 5, 6, 7, 8]
>>> c = a[:]
>>> c
['Hello', 2, 3, 4, 5, 6, 7, 8]
>>> a
['Hello', 2, 3, 4, 5, 6, 7, 8]
>>> a[1] = 'Python'
>>> a
['Hello', 'Python', 3, 4, 5, 6, 7, 8]
>>> b
['Hello', 'Python', 3, 4, 5, 6, 7, 8]
>>> c
['Hello', 2, 3, 4, 5, 6, 7, 8]
>>> id(c)
2399584626440
>>> id(a)
2399572778696
>>> a == b
True
>>> a is b
True
>>> a == c
False
>>> c = a[:]
>>> c
['Hello', 'Python', 3, 4, 5, 6, 7, 8]
>>> a
['Hello', 'Python', 3, 4, 5, 6, 7, 8]
>>> a == c
True
>>> a is c
False
>>> a = ['Hello', 'Python', 3,[ 4, 5, 6,] 7, 8]
SyntaxError: invalid syntax
>>> a = ['Hello', 'Python', 3,[ 4, 5, 6,],7, 8]
>>> d = a[:]
>>> d
['Hello', 'Python', 3, [4, 5, 6], 7, 8]
>>> a
['Hello', 'Python', 3, [4, 5, 6], 7, 8]
>>> a[-1] = 'Bye'
>>> a
['Hello', 'Python', 3, [4, 5, 6], 7, 'Bye']
>>> b
['Hello', 'Python', 3, 4, 5, 6, 7, 8]
>>> c
['Hello', 'Python', 3, 4, 5, 6, 7, 8]
>>> d
['Hello', 'Python', 3, [4, 5, 6], 7, 8]
>>> a[3][0] = 'Hi'
>>> a
['Hello', 'Python', 3, ['Hi', 5, 6], 7, 'Bye']
>>> d
['Hello', 'Python', 3, ['Hi', 5, 6], 7, 8]
>>> a[3] = 'Hello World'
>>> a
['Hello', 'Python', 3, 'Hello World', 7, 'Bye']
>>> d
['Hello', 'Python', 3, ['Hi', 5, 6], 7, 8]
>>> import copy
>>> a = ['Hello', 'Python', 3, ['Hi', 5, 6], 7, 'Bye']
>>> d = a[:]
>>> e = copy.deepcopy(a)
>>> a[3][0] = 'Bye'
>>> a
['Hello', 'Python', 3, ['Bye', 5, 6], 7, 'Bye']
>>> e
['Hello', 'Python', 3, ['Hi', 5, 6], 7, 'Bye']
>>> 
