# 4. Create a password validator function that takes in the password as its argument and returns an integer value you can evaluate to determine the password strength. Using the following validators:
#  0 -\&gt; very weak e.g. a password with only strings
#  1 -\&gt; weak e.g. a password with only numbers
#  2 -\&gt; strong e.g. a password containing strings and numbers
#  3 -\&gt; very strong e.g. a password containing strings, numbers and special characters (!,@,#,$,%, etc)
import re

passwordInput = input('Please enter a password: ')
# print(type(passwordInput))

def checkPassword(passwd):
    validator = ""
    w = re.search("[0-9]",passwd)
    x = re.search("[a-zA-Z]",passwd)
    y = re.fullmatch("[a-zA-Z0-9]",passwd)
    z = re.fullmatch(r'[a-zA-Z0-9][\w.-]+@[\w.-]+',passwd)
    while True:
        if w is None:
            print(0)
            print("password only contain strings")
            break
        if x is None:
            print(1)
            print("password only contain numbers")
            break
        if y is None:
            print(2)
            print("password contains strings and numbers")
            break
        if z is None:
            print(3)
            print("password contain strings, numbers, and special characters")
            break
    return validator

print(checkPassword(passwordInput))
