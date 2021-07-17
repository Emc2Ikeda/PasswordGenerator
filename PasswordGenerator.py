import random as rand
import string as str
import re

# check if PW is at least 8 chars long with at least 1 symbol, 1 number, 1 uppercase, and 1 lowercase
#def checkPassword(password):
#    if (len(password) < 8):
#        return False
#    elif (re.search('[0-9]', password) == None):
#        return False
#    elif (re.search('[a-z]', password) == None):
#        return False
#    elif (re.search('[A-Z]', password) == None):
#        return False
#    elif (re.search('[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]', password) == None):
#        return False
#    else:
#        return True

# generate random 8 char long PW with at least 1 symbol, 1 number, 1 uppercase, and 1 lowercase
def generatePassword(keyword=""):
    lower = str.ascii_lowercase
    upper = str.ascii_uppercase
    sym = str.punctuation
    num = str.digits

    # all possible characters for PW
    possibleChars = lower + upper + sym + num

    # randomly choose 8 chars for PW. If PW is invalid, regenerate new PW if invalid
    #password = ""
    # while (checkPassword(password) == False):
    #    password = ''.join(rand.choice(possibleChars) for _ in range(8))
    #if len(keyword) < 8:
    #    keyword += "**"

    # Convert keyword to list of chars, then add or replace chars to create a strong password
    keywordChars = [char for char in keyword]
    print(keywordChars)

    # TODO: modify this so that it replaces keyword w/ random char from matching pool
    if (re.search('[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]', keyword) == None):
        addSymbol = rand.choice(sym)
        keywordChars[7] = addSymbol
    if (re.search('[0-9]', keyword) == None):
        addNum = rand.choice(num)
        keywordChars[6] = addNum
    if (re.search('[a-z]', keyword) == None):
        addLowercase = rand.choice(lower)
        keywordChars[5] = addLowercase
    if (re.search('[A-Z]', keyword) == None):
        addUppercase = rand.choice(upper)
        keywordChars[4] = addUppercase
    
    # Re-convert to string
    keyword = "".join(keywordChars)
    print(keyword)
    #return keyword

# Console
keyword = input("Please enter the keyword to base password on: ")

#TODO: Replace this with adding more random characters to keyword
if len(keyword) < 8:
    print("Error: Keyword must be 8 characters long")
    keyword = input("Please enter the keyword to base password on: ")

# test: 10 tries
for _ in range(10):
    generatePassword(keyword)