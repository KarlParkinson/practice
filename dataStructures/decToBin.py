import stack


def decToBin(num):
    s = stack.Stack()
    while (num > 0):
        remainder = num % 2
        s.push(remainder)
        num = num // 2
    binString = ''
    while (not s.isEmpty()):
        binString += str(s.pop())
    return binString

def decToBase(num, base, chars):
    s = stack.Stack()
    while (num > 0):
        remainder = num % base
        s.push(chars[remainder])
        num = num // base
    baseString = ''
    while (not s.isEmpty()):
        baseString += s.pop()
    return baseString



print decToBin(8) # 1000
print decToBin(15) # 1111
print decToBin(33) # 100001

hexChars = '0123456789ABCDEF'
print decToBase(255, 8, hexChars)
