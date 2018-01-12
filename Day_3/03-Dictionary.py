Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dict_1 = {'id':101,'name':'Ram','age':18}
>>> dict_1[0]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    dict_1[0]
KeyError: 0
>>> dict_1['salary'] = 18000
>>> dict_1
{'id': 101, 'name': 'Ram', 'age': 18, 'salary': 18000}
>>> dict_1['id']
101
>>> dict_1['name']
'Ram'
>>> dict_1.keys()
dict_keys(['id', 'name', 'age', 'salary'])
>>> dict_1.values()
dict_values([101, 'Ram', 18, 18000])
>>> dict_1.items()
dict_items([('id', 101), ('name', 'Ram'), ('age', 18), ('salary', 18000)])
>>> dict_1
{'id': 101, 'name': 'Ram', 'age': 18, 'salary': 18000}
>>> for data in dict_1:
	print(data)

	
id
name
age
salary
>>> for data in dict_1.values():
	print(data)

	
101
Ram
18
18000
>>> for data in dict_1.items():
	print(data)

	
('id', 101)
('name', 'Ram')
('age', 18)
('salary', 18000)
>>> for data in dict_1.items():
	print(data[1])

	
101
Ram
18
18000
>>> emp = {'id' : [1,2,3,4,5,6], 'name' : ['Ram','Shyam','Lucky','Gopal','Ajay','Rahul']}
>>> emp
{'id': [1, 2, 3, 4, 5, 6], 'name': ['Ram', 'Shyam', 'Lucky', 'Gopal', 'Ajay', 'Rahul']}
>>> emp['id']
[1, 2, 3, 4, 5, 6]
>>> emp['id'][3]
4
>>> for data in emp.items():
	print(data)

	
('id', [1, 2, 3, 4, 5, 6])
('name', ['Ram', 'Shyam', 'Lucky', 'Gopal', 'Ajay', 'Rahul'])
>>> for data in emp.items():
	print(data[1])

	
[1, 2, 3, 4, 5, 6]
['Ram', 'Shyam', 'Lucky', 'Gopal', 'Ajay', 'Rahul']
>>> data
('name', ['Ram', 'Shyam', 'Lucky', 'Gopal', 'Ajay', 'Rahul'])
>>> for data in emp.items():
	print(data)

	
('id', [1, 2, 3, 4, 5, 6])
('name', ['Ram', 'Shyam', 'Lucky', 'Gopal', 'Ajay', 'Rahul'])
>>> for data in emp.items():
	for d in data:
		print(d)

		
id
[1, 2, 3, 4, 5, 6]
name
['Ram', 'Shyam', 'Lucky', 'Gopal', 'Ajay', 'Rahul']
>>> for data in emp.items():
	for d in data[1]:
		print(d)

		
1
2
3
4
5
6
Ram
Shyam
Lucky
Gopal
Ajay
Rahul
>>> for data in emp.items():
	print(data[0], data[1][0])

	
id 1
name Ram
>>> for data in emp.items():
	print(data[0], data[1][1])

	
id 2
name Shyam
>>> for data in emp.items():
	print(data[0], data[1][2])

	
id 3
name Lucky
>>> for i in range(7):
	for data in emp.items():
		print(data[0], data[1][i])

		
id 1
name Ram
id 2
name Shyam
id 3
name Lucky
id 4
name Gopal
id 5
name Ajay
id 6
name Rahul
Traceback (most recent call last):
  File "<pyshell#47>", line 3, in <module>
    print(data[0], data[1][i])
IndexError: list index out of range
>>> 
