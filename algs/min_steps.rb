def min_steps(steps_arr)
  min_steps = [nil]*steps_arr.length
  min_steps[steps_arr.length - 1] = 0
  j = steps_arr.length - 2
  while (j >= 0)
    steps = steps_arr[j]
    min_s = 1.0/0
    (1..steps).each do |step_size|
      s = if (j + step_size < steps_arr.length) then min_steps[j+step_size] else 0 end
      s += 1
      if (s < min_s)
        min_s = s
      end
    end
    min_steps[j] = min_s
    j -= 1
  end
  return min_steps[0]
end




a = [2,0,5,8,9,2,6,7,6,8,9]
puts min_steps(a)
