import binTree

def constructParseTree(expr):
    print expr
    if (expr == []):
        return
    expTree = binTree.BinaryTree('')
    for char in expr:
        if (char == '('):
            expTree.leftChild = constructParseTree(expr[1:])
        elif (char in '+-*/'):
            expTree.setRootVal(char)
            expTree.rightChild = constructParseTree(expr[1:])
        elif (char in '0123456789'):
            expTree.setRootVal(char)
#            return expTree
        elif (char == ')'):
            return expTree
    return expTree



constructParseTree(list('((7+3)*(5-2))')).inorder()
