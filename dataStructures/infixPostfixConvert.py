import stack

def infixToPostfix(expr):
    s = stack.Stack()
    prec = {"*":3, "/":3, "+":2, "-":2, "(":1}
    ops = "*/+-("
    postfixString = ""
    for char in expr:
        if (char in ops):
            lower = False
            while (not s.isEmpty() and not lower and char != '('):
                op = s.peek()
                if (prec[op] < prec[char]):
                    lower = True
                else:
                    postfixString += s.pop()
            s.push(char)
        elif (char == ')'):
            op = s.pop()
            while (op != '('):
                postfixString += op
                op = s.pop()
        else:
            postfixString += char
    while (not s.isEmpty()):
        postfixString += s.pop()
    return postfixString


#print infixToPostfix("A+B*C")
#print infixToPostfix("A+B+C+D")
#print infixToPostfix("A+B*C+D")
print infixToPostfix("(A+B)*(C+D)")
#print infixToPostfix("A*B+C*D")

