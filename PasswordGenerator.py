import random as rand
import string as str
import re

# generate random 8 char long PW with at least 1 symbol, 1 number, 1 uppercase, and 1 lowercase
def generatePassword(keyword=""):
    lower = str.ascii_lowercase
    upper = str.ascii_uppercase
    sym = str.punctuation
    num = str.digits
    possibleChars = lower + upper + sym + num

    # add chars to make it 8 chars long if len(keyword) < 8 
    if (len(keyword < 8)):
        keyword = addChars(keyword)

    # Convert keyword to list of chars, then add or replace chars
    keywordChars = [char for char in keyword]
    charsToReplace = rand.sample(range(0,len(keyword)), k=4)

    if (re.search('[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]', keyword) == None):
        keywordChars[charsToReplace[0]] = rand.choice(sym)
    if (re.search('[0-9]', keyword) == None):
        keywordChars[charsToReplace[1]] = rand.choice(num)
    if (re.search('[a-z]', keyword) == None):
        keywordChars[charsToReplace[2]] = rand.choice(lower)
    if (re.search('[A-Z]', keyword) == None):
        keywordChars[charsToReplace[3]] = rand.choice(upper)
    
    # Re-convert to string
    keyword = "".join(keywordChars)
    print(keyword)

def addChars(keyword):
    return keyword+'xxxx'

# Console
print("Select password length: ")
# TODO: add error handling to accept only integers
length = int(input())
keyword = input("Please enter the keyword to base password on: ")

if len(keyword) < length or len(keyword) < 8:
    if (length > 8):
        # TODO: add characters to make it 8 chars long
        print("Error: Keyword must be" + length + "characters long")
    else:
        print("Error: Keyword must be 8 characters long")
    print("Your password is " + addChars(keyword))

# test: 10 tries
for _ in range(10):
    generatePassword(keyword)