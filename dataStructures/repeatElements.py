def repeatedElements(arr):
    for i in xrange(len(arr)):
        element = arr[i]
        for j in xrange(i+1, len(arr)):
            if (arr[j] == element):
                print element



repeatedElements([4,2,4,5,2,3,1])
