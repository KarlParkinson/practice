def stairs(n,m)
  ways = [0]*n
  ways[0] = 1
  ways[1] = 2
  (2..(n-1)).each do |i|
    s = 0
    (1..m).each do |j|
      s += ways[i-j] if (i-j >= 0)
    end
    ways[i] = s
  end
  return ways[n-1]
end



puts stairs(4,2)
