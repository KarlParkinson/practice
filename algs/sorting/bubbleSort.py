def bubbleSort(lst):
    for i in xrange(len(lst)):
        j = 0
        while (j < len(lst)-1):
            if (lst[j] > lst[j+1]):
                # swap elements
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
            j += 1

def bubbleSort2(lst):
    swapped = True
    while (swapped):
        swapped = False
        j = 0
        while (j < len(lst)-1):
            if (lst[j] > lst[j+1]):
                lst[j],lst[j+1] = lst[j+1],lst[j]
                swapped = True
            j += 1


lst = [9,8,7,6,5]
bubbleSort2(lst)
print lst
