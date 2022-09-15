import pytest 
from passwdGenerate import passwdLength, usrPassword

def passwdLengthFunc():
    return passwdLength

def userPassword():
    return usrPassword

# testing user password legth input. Test passes if user input length matches password length
def test_passwdLength_input():
    assert passwdLengthFunc() == len(usrPassword)
    
# testing to check if generated password is a string
def test_password_is_string():
    assert isinstance(userPassword(), str)

    

