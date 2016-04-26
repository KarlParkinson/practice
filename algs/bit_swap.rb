def bit_swap(x,p1,p2,n)
  (0..(n-1)).each do |i|
    # get bit at p1
    j = p1 + i
    mask = 1 << j
    first_bit = x & mask
    first_bit >>= j
    # get bit at p2
    k = p2 + i
    mask = 1 << k
    second_bit = x & mask
    second_bit >>= k
    # clear p1 bit in x
    x = x & ~(1 << j)
    # set p1 bit to be p2 bit
    x |= (second_bit << j)
    # clear p2 bit in x
    x = x & ~(1 << k)
    # set p2 bit to be p1 bit
    x |= (first_bit << k)
  end
  return x
end


z = bit_swap(47,1,5,3)
y = bit_swap(28,0,3,2)

puts "%08b" % z
puts "%08b" % y
