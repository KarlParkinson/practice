def merge_sort(arr)
  if (arr.length <= 1)
    return arr
  end
  half_index = arr.length / 2
  first_half = arr[0..half_index-1]
  second_half = arr[half_index..arr.length-1]
  
  sorted_one = merge_sort(first_half)
  sorted_two = merge_sort(second_half)

  i = 0
  j = 0

  sorted = []
  while (i < sorted_one.length and j < sorted_two.length)
    if (sorted_one[i] <= sorted_two[j]) 
      sorted << sorted_one[i]
      i = i + 1
    else
      sorted << sorted_two[j]
      j = j + 1
    end
  end

  while (i < sorted_one.length)
    sorted << sorted_one[i]
    i = i + 1
  end

  while (j < sorted_two.length)
    sorted << sorted_two[j]
    j = j + 1
  end

  return sorted

end


begin
  test1 = [3,1,5,4,9]
  s = merge_sort(test1)
  puts s.to_s
end
