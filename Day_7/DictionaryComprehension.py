Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = {x : x**2 for x in range(1,11)}
>>> a
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
>>> names = ['Ram','Shyam','Anuj','Ajay','Ankur']
>>> data = {'name' : name for name in names}
>>> data
{'name': 'Ankur'}
>>> data = {'name_'+str(i+1) : name for i,name in enumerate(names)}
>>> data
{'name_1': 'Ram', 'name_2': 'Shyam', 'name_3': 'Anuj', 'name_4': 'Ajay', 'name_5': 'Ankur'}
>>> for i in names:
	print(i)

	
Ram
Shyam
Anuj
Ajay
Ankur
>>> for i in enumerate(names):
	print(i)

	
(0, 'Ram')
(1, 'Shyam')
(2, 'Anuj')
(3, 'Ajay')
(4, 'Ankur')
>>> for index,name in enumerate(names):
	print(index,name)

	
0 Ram
1 Shyam
2 Anuj
3 Ajay
4 Ankur
>>> for i in enumerate(names):
	print(i[0])

	
0
1
2
3
4
>>> for i in enumerate(names):
	print(i[0],i[1])

	
0 Ram
1 Shyam
2 Anuj
3 Ajay
4 Ankur
>>> dict_1 = {'name':'Ram','name':'Shyam'}
>>> dict_1
{'name': 'Shyam'}
>>> 
