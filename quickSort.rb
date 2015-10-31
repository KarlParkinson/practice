def quick_sort(arr, from, to)
  if (to <= from)
    return arr
  end

  p = partition(arr, from, to)
  quick_sort(arr, from, p-1)
  quick_sort(arr, p+1, to)
 
end

def partition(arr, from, to)
  pivot = arr[from..to].sample
  i = from
  j = to
  while (i <= j)
    while (arr[i] < pivot)
      i = i + 1
    end
    while (arr[j] > pivot)
      j = j - 1
    end
    if (i <= j)
      tmp = arr[i]
      arr[i] = arr[j]
      arr[j] = tmp
      i = i + 1
      j = j - 1
    end
  end
  return i
end


begin
  test1 = [3,1,5,4,9]
  quick_sort(test1, 0, test1.length-1)
  puts test1.to_s
  test2 = [9,3]
#  quick_sort(test2,0,1)
#  puts test2.to_s
end
