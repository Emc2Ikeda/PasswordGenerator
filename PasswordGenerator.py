import random as rand
import string as str
import re

# check if PW is at least 8 chars long with at least 1 symbol, 1 number, 1 uppercase, and 1 lowercase
def checkPassword(password):
    if (len(password) < 8):
        return False
    elif (re.search('[0-9]', password) == None):
        return False
    elif (re.search('[a-z]', password) == None):
        return False
    elif (re.search('[A-Z]', password) == None):
        return False
    elif (re.search('[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]', password) == None):
        return False
    else:
        return True

# generate random 8 char long PW with at least 1 symbol, 1 number, 1 uppercase, and 1 lowercase
def generatePassword():
    lower = str.ascii_lowercase
    upper = str.ascii_uppercase
    sym = str.punctuation
    num = str.digits

    # all possible characters for PW
    possibleChars = lower + upper + sym + num

    # randomly choose 8 chars for PW. If PW is invalid, regenerate new PW if invalid
    password = ""
    while (checkPassword(password) == False):
        password = ''.join(rand.choice(possibleChars) for _ in range(8))
    print("Your password is: " + password)

# 10 tries
for _ in range(10):
    generatePassword()