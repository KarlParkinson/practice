import stack

def insertAtBottom(s, item):
    if (s.isEmpty()):
        s.push(item)
    else:
        temp = s.pop()
        insertAtBottom(s, item)
        s.push(temp)


def reverse(s):
    if (not s.isEmpty()):
        temp = s.pop()
        reverse(s)
        insertAtBottom(s, temp)


s = stack.Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

print s.items
reverse(s)
print s.items
