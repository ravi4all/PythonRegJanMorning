def evenCheck(num):
    return num % 2 == 0

numbers = []

for n in range(0,51):
    numbers.append(n)

# even = list(map(evenCheck, numbers))
even = list(filter(evenCheck, numbers))
print(even)