def subsets(arr)
  num_subsets = 1 << arr.length
  subsets = []
  (0..num_subsets).each do |i|
    subset = []
    pos = arr.length - 1
    bitmask = i
    while (bitmask > 0)
      if ((bitmask & 1) == 1)
        subset << arr[pos]
      end
      bitmask >>= 1
      pos -= 1
    end
    subsets << subset
  end
  return subsets
end


puts subsets([1,2,3,4,5,6]).to_s
