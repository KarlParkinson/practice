def search(pat, txt)
  n = txt.length
  m = pat.length
  (0..(n-m)).each do |i|
    match = true
    (0..(m-1)).each do |j|
      if (pat[j] != txt[i+j])
        match = false
      end
    end
    if (match)
      puts "pattern found at index %d" % i
    end
  end
end



search("test", "this is a test text")
search("AABA", "AABAACAADAABAAABAA")
