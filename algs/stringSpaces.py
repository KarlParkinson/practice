def stringSpaces(string):
    buff = ['']*(2*len(string))
    
    buff[0] = string[0]
    i = 1
    j = 1
    stringSpacesUtil(string, i, j, buff, len(string))

def stringSpacesUtil(string, i, j, buff, n):
    if (i == n):
        print ''.join(buff)
        return
    
    # put character at position j
    buff[j] = string[i]
    stringSpacesUtil(string, i+1, j+1, buff, n)

    # put space at position j
    buff[j] = ' '
    buff[j+1] = string[i]
    stringSpacesUtil(string, i+1, j+2, buff, n)



stringSpaces("ABCD")
