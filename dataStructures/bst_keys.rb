require_relative 'binTree'

def bst_keys(bst, k1, k2)
  if (bst.nil?)
    return
  end
  if (k1 < bst.key)
    bst_keys(bst.left_child, k1, k2)
  end
  if ((k1 <= bst.key) and (bst.key <= k2))
    puts bst.key
  end
  if (k2 > bst.key)
    bst_keys(bst.right_child, k1, k2)
  end
end


begin
  bst = BinarySearchTree.new(20, 'a')
  bst.insert(8, 'j')
  bst.insert(4, 'p')
  bst.insert(12, 'm')
  bst.insert(35, 'h')
  bst.insert(26, 'm')
  bst.insert(38, 'o')
#  puts bst.inspect
#  puts ""
  bst_keys(bst, 25, 40)
end
