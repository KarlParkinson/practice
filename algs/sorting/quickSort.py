def quicksort(lst, left, right):
    if (left >= right):
        return
    #p = partition(lst, left, right)
    p = partition2(lst, left, right)
    quicksort(lst, left, p-1)
    quicksort(lst, p+1, right)


def partition(lst, left, right):
    pivotVal = lst[left]
    i = left+1
    j = right
    while (i <= j):
        while (i <= j and lst[i] <= pivotVal):
            i += 1
        while (lst[j] >= pivotVal and j >= i):
            j -= 1
        if (i <= j):
            lst[i], lst[j] = lst[j], lst[i]
    lst[left], lst[j] = lst[j], lst[left]
    return j

def partition2(lst, left, right):
    pivotVal = lst[left]
    s = left
    i = left+1
    while (i <= right):
        if (lst[i] < pivotVal):
            s += 1
            lst[s],lst[i] = lst[i],lst[s]
        i += 1
    lst[left],lst[s] = lst[s],lst[left]
    return s


lst = [3,8,6,5,9,2]
quicksort(lst, 0, len(lst)-1)
print lst
