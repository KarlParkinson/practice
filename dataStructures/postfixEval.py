import stack
from operator import add, div, mul, sub

def postfixEval(expr):
    s = stack.Stack()
    ops = "+-/*"
    opFuncs = {"+":add, "-":sub, "*":mul, "/":div}
    for char in expr:
        if (char in ops):
            operand2 = int(s.pop())
            operand1 = int(s.pop())
            s.push(opFuncs[char](operand1, operand2))
        else:
            s.push(char)
    return s.pop()



print postfixEval('89+') # 17
print postfixEval('239*+') # 29
print postfixEval('92-') # 7
print postfixEval('84/') # 2
print postfixEval('82/1-') # 3
            
