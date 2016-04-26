def egg_drops(eggs, floors)
  minDrops = makeMatrix[eggs, floors]

  (0..(floors-1)).each do |j|
    minDrops[0][j] = j+1
  end

  (0..(eggs-1)).each do |i|
    minDrops[i][0] = 1
  end

  (1..(eggs-1)).each do |i|
    (1..(floors-1)).each do |j|
      minDrops[i][j] = [minDrops[i-1][j-1], minDrops[[i][floors-j]
    end
  end
    
