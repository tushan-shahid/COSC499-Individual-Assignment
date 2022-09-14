import string
import random 

print("Welcome to Password Generator")
print("*****************************")

passwdLength = int(input("Input length of password: "))

passwdChars = list(string.ascii_lowercase + string.ascii_uppercase)

random.shuffle(passwdChars)

print(passwdChars)

password = []
for i in range(passwdLength):
    password.append(random.choice(passwdChars))
    
print(password)

usrPassword=""
for i in password:
    usrPassword+=i

print(f"Your generated password is: {usrPassword}")

    

