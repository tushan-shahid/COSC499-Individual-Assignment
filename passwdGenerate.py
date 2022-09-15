import string
import random 

print("Welcome to Password Generator")
print("*****************************\n")
    
passwdLength = int(input("Input length of password: "))
passwdType = int(input("Enter Choice (1 to include characters and numbers, 2 to include numbers and symbols, 3 to include characters, numbers and symbols): "))

passwdStr = list(string.ascii_lowercase + string.ascii_uppercase)
passwdInt = list(string.digits)
passwdSym = list("!@#$%^&*()_+?><~")

choice1 = passwdStr+passwdInt
choice2 = passwdInt+passwdSym
choice3 = passwdStr+passwdInt+passwdSym

if passwdType == 1:
    
    # if(passwdType==1):
    random.shuffle(choice1)

    password = []

    for i in range(passwdLength):
        password.append(random.choice(choice1))

    usrPassword=""
    for i in password:
        usrPassword+=i

    print(f"Your generated password is: {usrPassword}\n")
elif passwdType == 2:
        
    # if(passwdType==2 ):
    random.shuffle(choice2)

    password = []

    for i in range(passwdLength):
        password.append(random.choice(choice2))

    usrPassword=""
    for i in password:
        usrPassword+=i

    print(f"Your generated password is: {usrPassword}\n")
else :
     # if(passwdType==3):
    random.shuffle(choice3)

    password = []

    for i in range(passwdLength):
        password.append(random.choice(choice3))

    usrPassword=""
    for i in password:
        usrPassword+=i

    print(f"Your generated password is: {usrPassword}\n")
    
print("************************END***************************")

    

