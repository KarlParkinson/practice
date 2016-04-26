def reverse(str)
  i = str.length-1
  j = 0
  while (j < i)
    t = str[j]
    str[j] = str[i]
    str[i] = t
    i = i - 1
    j = j + 1
  end
  return str
end

def reverseCooler(str)
  half = str.length / 2
  half.times do |i|
    str[i], str[-i-1] = str[-i-1], str[i]
  end
  return str
end


begin
  test1 = 'hello'
  puts reverse(test1) # should be 'olleh'
  puts test1
  test2 = 'this'
  #puts reverse(test2) # should be 'siht'
#  puts reverseCooler(test1)
#  puts reverseCooler(test2)
end
  
    
