import time

def removeChars(string, remove):
    string = list(string)
    for char in remove:
        while (char in string):
            string.remove(char)
    return ''.join(string)

def removeChars2(string, remove):
    removeDict = {char:True for char in remove}
    newString = ''
    for char in string:
        if (char not in removeDict):
            newString += char
    return newString

def removeChars3(string, remove):
    removeDict = {char:True for char in remove}
    string = list(string)
    for j in xrange(len(string)):
        if (string[j] in removeDict):
            string[j] = ''
    return ''.join(string)

s = "kaarrbcl"
r = "arb"
start = time.time()
removeChars(s, r)
print time.time() - start
start = time.time()
removeChars2(s, r)
print time.time() - start
start = time.time()
removeChars3(s, r)
print time.time() - start
