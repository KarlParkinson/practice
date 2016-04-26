import stack

def isBalanced(expr):
    s = stack.Stack()
    for paren in expr:
        if (paren == '('):
            s.push(paren)
        elif (paren == ')'):
            if (s.isEmpty()):
                return False
            s.pop()
    return True if s.isEmpty() else False


a = '()'
b = '(())'
c = '(((()()())))'
d = '((((('
e = '((((()'
f = '(((())'
g = '))'

print isBalanced(a) # True
print isBalanced(b) # True
print isBalanced(c) # True
print isBalanced(d) # False
print isBalanced(e) # False
print isBalanced(f) # False
print isBalanced(g) # False
