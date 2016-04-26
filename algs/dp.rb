def coin_row(coins)
  change = []
  change[0] = 0
  change[1] = coins[0]
  (2..coins.length).each do |i|
    if ((coins[i-1] + change[i-2]) > change[i-1])
      change[i] = coins[i-1] + change[i-2]
    else
      change[i] = change[i-1]
    end
  end
  return change.pop, coins_used
end

def change_make(denoms, amount)
  coins_used = []
  coins_used[0] = 0
  min_table = []
  min_table[0] = 0
  (1..amount).each do |i|
    coin_count = i
    new_coin = 1
    denoms.select {|d| d <= i}.each do |j|
      if ((min_table[i-j] + 1) < coin_count)
        # found new minimum amount of coins
        coin_count = min_table[i-j] + 1
        new_coin = j
      end
    end
    min_table[i] = coin_count
    coins_used[i] = new_coin
  end

  used = []
  j = amount
  while (j > 0)
    used << coins_used[j]
    j = j - coins_used[j]
  end
  return min_table[amount], used
end

def max(a,b)
  if (a>b) then a else b end
end

def rod_cutting(prices, length)
  max_vals = []
  max_vals[0] = 0
  (1..length).each do |i|
    max_price = prices[i-1]
    (1..i).each do |cut|
      max_price = max(max_price, prices[cut-1] + max_vals[i-cut])
    end
    max_vals[i] = max_price
  end
  return max_vals[length]
end


begin
  #puts change_make([1,3,4], 20).to_s
  puts rod_cutting([1,5,8,9,10,17,17,20], 5)
#  coins = [5,1,2,10]#,6,2]
#  puts coin_row(coins).to_s
#  puts coins.to_s
end
