file = open('file_2.txt', 'w')

data = {'Name' : 'Ram', 'Age' : 21}

file.write(str(data).strip("{}"))

file.close()