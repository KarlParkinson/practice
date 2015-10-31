def str_reverse(str)
  i = 0
  j = str.length - 1
  while (i < j)
    tmp = str[j]
    str[j] = str[i]
    str[i] = tmp
    i = i + 1
    j = j - 1
  end
end

def str_reverse_cooler(str)
  half = str.length / 2
  half.times do |i|
    str[i],str[-i-1] = str[-i-1],str[i]
  end
end

def fib(n)
  if (n > 1) then return fib(n-1) + fib(n-2) else return n end
end

def grade_school_mult(n)
  (1..n).each do |i|
    (1..n).each do |j|
      printf("%4d", i*j)
    end
    printf("\n")
  end
end

def text_file_sum(file_name)
  file_sum = 0
  File.open(file_name, 'r') do |f|
    f.readlines.each do |line|
      file_sum += line.to_i
    end
  end
  return file_sum
end

def text_file_sum_less_mem(file_name)
  file_sum = 0
  File.open(file_name, 'r') do |f|
    while (!f.eof?)
      file_sum += f.readline.to_i
    end
  end
  return file_sum
end

def print_odd_nums
  (1..99).each do |i|
    puts i if (i%2 == 1)
  end
end

def largest_int_in_array(arr)
  max = arr[0]
  i = 0
  while(i < arr.length)
    if (arr[i] > max)
      max = arr[i]
    end
    i += 1
  end
  return max
end
  


begin
#  puts fib(0)
#  puts fib(1)
#  puts fib(5)
#  grade_school_mult(12)
#  puts text_file_sum('test_file_sum.txt')
#  puts text_file_sum_less_mem('test_file_sum.txt')
#  print_odd_nums
  puts largest_int_in_array([0,10,2,3,4,99,100,45])
end
