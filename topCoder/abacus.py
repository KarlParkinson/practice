def add(original, val):
    num = int(whatNumber(original))
    new = num + val
    return toAbacus(str(new))

def whatNumber(abacus):
    num = ''
    exponent = len(abacus) - 1
    for j in xrange(len(abacus)):
        row = abacus[j].split("---")
        dig = len(row.pop())
        num += str(dig) 
    return num

def toAbacus(num):
    abacus = []
    for digit in num:
        d = int(digit)
        thread = (9-d)*'o' + '---' + d*'o'
        abacus.append(thread)
    return abacus

print add(["ooo---oooooo", "---ooooooooo", "---ooooooooo", "---ooooooooo", "oo---ooooooo", "---ooooooooo"], 5)
