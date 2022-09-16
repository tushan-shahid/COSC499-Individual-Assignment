import pytest 
import string
from passwdGenerate import passwdLength, usrPassword, passwdType, passwdInt, passwdSym, passwdStr

def passwdLengthFunc():
    return passwdLength

def userPassword():
    return usrPassword

def typeOfPassword():
    return passwdType


# testing user password legth input. Test passes if user input length matches password length
def test_passwdLength_input():
    assert passwdLengthFunc() == len(usrPassword)
    
# testing to check if generated password is a string
def test_password_is_string():
    assert isinstance(userPassword(), str)

# testing to check if password choice type is right 
def test_password_is_str_int():
    if passwdType == 1:
        if any(c in passwdStr and passwdInt for c in userPassword()):
            assert True
        else:
            assert False
    elif passwdType == 2:
        if any(c in passwdInt and passwdSym for c in userPassword()):
            assert True
        else:
            assert False    
    elif passwdType == 3:
        if any(c in passwdStr and passwdInt and passwdSym for c in userPassword()):
            assert True
        else:
            assert False
        


