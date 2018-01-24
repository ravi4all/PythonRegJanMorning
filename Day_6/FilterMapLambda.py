# add = lambda x,y : x + y
# print(add(2,4))

users = [{"id":101,"name":"Ram","age":25},
         {"id": 102, "name": "Shyam", "age": 28},
         {"id": 103, "name": "Aman", "age": 22},
         {"id": 104, "name": "Kishor", "age": 25},
         {"id": 105, "name": "Tom", "age": 21},
         {"id": 106, "name": "John", "age": 24}]

# def sortBy(x):
#     return x['age']

# sortedUserList = sorted(users, key=sortBy)
sortedUserList = sorted(users, key= lambda x : x['age'])
print(sortedUserList)

# for user in users:
#     print(user['age'])

# def filterUser(x):
#     if x['age'] > 24:
#         return x['age']
#     else:
#         return "Not greater than 24"

# for user in users:
#     print(filterUser(user))

def filterUser(x):
    return x['age'] > 24

# filteredList = list(filter(filterUser, users))
filteredList = list(filter(lambda x : x['age'] > 24, users))
print(filteredList)