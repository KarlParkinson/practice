def pos_set_bit(x)
  p = 0
  while (x != 0)
    x >>= 1
    p += 1
  end
  return p
end


puts pos_set_bit(-1)
