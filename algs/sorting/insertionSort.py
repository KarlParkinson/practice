def insertionSort(lst):
    for i in xrange(len(lst)):
        j = i
        while (lst[j] < lst[j-1] and j > 0):
            # swap
            lst[j],lst[j-1] = lst[j-1],lst[j]
            j -= 1


lst = [9,8,5,7,6,5]
insertionSort(lst)
print lst
