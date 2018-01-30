file = open('file_1.txt')

# data = file.read()

# data = file.readline()

# data = file.readlines()

data = file.read(15)
print(data)

file.close()