def mergeSort(lst):
#    print lst
    if (len(lst) == 1):
        return lst
    mid = len(lst)/2
    left = lst[:mid]
    right = lst[mid:]
    
    mergeSort(left)
    mergeSort(right)
    merge(left, right, lst)

def merge(A, B, lst):
    i = 0
    j = 0
    k = 0
    
    while (i < len(A) and j < len(B)):
        if (A[i] <= B[j]):
            lst[k] = A[i]
            i += 1
        elif (B[j] < A[i]):
            lst[k] = B[j]
            j += 1
        k += 1

    while (i < len(A)):
        # B ran out first
        lst[k] = A[i]
        i += 1
        k += 1

    while (j < len(B)):
        # A ran out first
        lst[k] = B[j]
        j += 1
        k += 1



lst = [9,8,7,6,5]
mergeSort(lst)

print lst

