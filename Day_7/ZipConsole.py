Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> str_1 = "Hello this is python programming and python is used for Machine learning"
>>> set(str_1)
{'u', 'm', 'a', 'e', 'f', 'i', 'p', 'H', 'g', 'o', 't', 'r', 'l', 'n', 'd', 'y', 'c', 'M', ' ', 'h', 's'}
>>> str_1.split()
['Hello', 'this', 'is', 'python', 'programming', 'and', 'python', 'is', 'used', 'for', 'Machine', 'learning']
>>> x = set(str_1.split())
>>> str_2 = "This is python and python is used for Machine learning"
>>> y = set(str_1.split())
>>> x = set(str_1.split())
>>> y = set(str_2.split())
>>> x
{'and', 'learning', 'Hello', 'python', 'Machine', 'programming', 'is', 'this', 'used', 'for'}
>>> y
{'and', 'learning', 'python', 'Machine', 'is', 'This', 'used', 'for'}
>>> x & y
{'learning', 'and', 'python', 'Machine', 'is', 'used', 'for'}
>>> x | y
{'and', 'learning', 'Hello', 'python', 'Machine', 'programming', 'is', 'This', 'this', 'used', 'for'}
>>> len(x & y) / len(x | y)
0.6363636363636364
>>> x
{'and', 'learning', 'Hello', 'python', 'Machine', 'programming', 'is', 'this', 'used', 'for'}
>>> y
{'and', 'learning', 'python', 'Machine', 'is', 'This', 'used', 'for'}
>>> list_1 = [1,2,3,4,5,6,7,8]
>>> list_2 = ['Ram','Shyam','Anuj','Sumit','Gaurav','Salman','amir','Gopal']
>>> for id in range(len(list_1)):
	print(list_1[id],list_2[id])

	
1 Ram
2 Shyam
3 Anuj
4 Sumit
5 Gaurav
6 Salman
7 amir
8 Gopal
>>> zip(list_1,list_2)
<zip object at 0x0000022A52B0A848>
>>> list(zip(list_1,list_2))
[(1, 'Ram'), (2, 'Shyam'), (3, 'Anuj'), (4, 'Sumit'), (5, 'Gaurav'), (6, 'Salman'), (7, 'amir'), (8, 'Gopal')]
>>> z = list(zip(list_1,list_2))
>>> for data in z:
	print(data)

	
(1, 'Ram')
(2, 'Shyam')
(3, 'Anuj')
(4, 'Sumit')
(5, 'Gaurav')
(6, 'Salman')
(7, 'amir')
(8, 'Gopal')
>>> for data in zip(list_1,list_2):
	print(data)

	
(1, 'Ram')
(2, 'Shyam')
(3, 'Anuj')
(4, 'Sumit')
(5, 'Gaurav')
(6, 'Salman')
(7, 'amir')
(8, 'Gopal')
>>> 
