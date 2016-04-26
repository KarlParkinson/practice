def selectionSort(lst):
    for i in xrange(len(lst)):
        minIndex = i
        for j in xrange(i+1, len(lst)):
            if (lst[j] < lst[minIndex]):
                minIndex = j
        # swap minIndex and i
        lst[i],lst[minIndex] = lst[minIndex],lst[i]


lst = [9,8,7,6,5]
selectionSort(lst)
print lst
