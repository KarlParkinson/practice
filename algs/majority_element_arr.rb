def majority(arr)
  dic = {}
  maj = arr.length / 2
  arr.each do |i|
    if (dic[i].nil?)
      dic[i] = 1
    else
      dic[i] += 1
      if (dic[i] > maj)
        puts i
        return
      end
    end
  end
  puts "NONE"
end


a = [3,3,4,2,4,4,2,4,4]
majority(a)
b = [3,3,4,2,4,4,2,4]
majority(b)
