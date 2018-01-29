from datetime import datetime

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

    userOptions()

def viewProfile(username, usermail):
    pass

def updateProfile(username, usermail):
    pass

def deleteProfile(username, usermail):
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
        "4" : deleteProfile
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

while True:
    print("""
    1. Login
    2. Regsitration
    """)

    user_choice = input("Enter your choice : ")

    choices = {
        "1" : login,
        "2" : register
    }
    choices.get(user_choice)()

