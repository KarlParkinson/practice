def str_reverse(string):
    newStr = list(string)
    i = 0
    j = len(string) - 1
    while (i < j):
        tmp = newStr[j]
        newStr[j] = newStr[i]
        newStr[i] = tmp
        i += 1
        j -= 1
    return "".join(newStr)

def str_reverse_cooler(string):
    newStr = list(string)
    half = len(string) / 2
    for i in range(0,half):
        newStr[i],newStr[-i-1] = newStr[-i-1],newStr[i]
    return "".join(newStr)

def fib(n):
    # if (n > 1) return fib(n-1) + fib(n-2) else return n
    if (n == 1):
        return 0
    elif (n == 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

def mult_table(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
#            k = i*j
            print('%4d' % int(i*j)),
#            print("%d" % i*j),
        print("")

def text_file_sum(file_name):
    # could also use with open(file_name, 'r') as f:...
    f = open(file_name, 'r')
    fileSum = 0
    for line in f:
        fileSum += int(line.rstrip('\n'))
    f.close()
    return fileSum

def text_file_sum2(file_name):
    f = open(file_name, 'r')
    nums = f.readlines()
    f.close()
    return sum(map(int,nums))

def print_odd_nums():
#    odd_nums = [i for i in range(1,100) if i%2 ==1]
#    print(odd_nums)
    for i in range(1,100):
        if (i%2 == 1):
            print(i)

def largest_int_in_array(arr):
    max_elem = arr[0]
    for i in arr:
        if (i > max_elem):
            max_elem = i
    return max_elem


#test_str1 = 'butt'
#print (str_reverse(test_str1))
#print (str_reverse_cooler(test_str1))
#print(fib(1)) # 0
#print(fib(2)) # 1
#print(fib(3)) # 1
#print(fib(6)) # 5
#mult_table(12)
#print(text_file_sum('test_file_sum.txt'))
#print(text_file_sum2('test_file_sum.txt'))
#print_odd_nums()
print(largest_int_in_array([1,2,3,9,7,5]))
