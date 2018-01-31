from datetime import datetime
import csv

users = []
userData = {}
allPosts = []

def post(username, usermail):
    print("Welcome {}, Post Here...".format(username))
    userPost = {}

    user_post = input("Enter your post : ")
    postTime = datetime.now().time()
    userPost['userName'] = username
    userPost['userPost'] = user_post
    userPost['time'] = postTime

    allPosts.append(userPost.copy())

    for posts in allPosts:
        print(posts)

    userOptions(username,usermail)

def viewProfile(username, usermail):
    print("User Profile : ")
    print("Username : {} UserEmail : {}".format(username,usermail))
    currentUserpost = list(filter(lambda x:x['userName'] == username, allPosts))
    print("Your Posts : ")
    # print(currentUserpost)
    for currentPost in currentUserpost:
        print("Post :",currentPost['userPost'])
        print("Time :",currentPost['time'])

    userOptions(username, usermail)


def updateProfile(username, usermail):
    pass

def deleteProfile(username, usermail):
    pass

def logout(x,y):
    pass

def userOptions(username, useremail):
    print("""
    1. Post Something
    2. View Profile
    3. Update Profile
    4. Delete Profile
    5. Logout
    """)

    todo = {
        "1" : post,
        "2" : viewProfile,
        "3" : updateProfile,
        "4" : deleteProfile,
        "5" : logout
    }

    userchoice = input("Enter your choice : ")
    todo.get(userchoice)(username, useremail)


def login():
    useremail = input("Enter EmailId : ")
    userpwd = input("Enter password : ")

    for user in users:
        if useremail in user['userEmail']:
            if user['userEmail'] == useremail and user['password'] == userpwd:
                print("Welcome",user['userName'])
                userOptions(user['userName'], user['userEmail'])
            else:
                print("Invalid EmailId or Password")


def register():
    username = input("Enter your name : ")
    while True:
        userpwd = input("Enter your password : ")
        confirmpwd = input("Confirm password : ")
        if userpwd == confirmpwd:
            break
        else:
            print("Password do not match")
            print("Re-enter password")

    while True:
        useremail = input("Enter your email : ")
        if '@' in useremail:
            break
        else:
            print("Invalid email")

    userData['userName'] = username
    userData['userEmail'] = useremail
    userData['password'] = userpwd

    users.append(userData.copy())
    print("Data Inserted Successfully...")
    read()

def read():
    for data in users:
        print(data)

    saveUser()

def saveUser():
    with open('users.csv','a',newline='') as file:
        writer = csv.writer(file)

        writer.writerow(users[-1].values())

while True:
    print("""
    1. Login
    2. Registration
    """)

    user_choice = input("Enter your choice : ")

    choices = {
        "1" : login,
        "2" : register
    }
    choices.get(user_choice)()

