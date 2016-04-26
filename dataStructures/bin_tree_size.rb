require_relative 'binTree'

def size(bin_tree)
  if (bin_tree.nil?)
    return 0
  else
    return 1 + size(bin_tree.get_left_child) + size(bin_tree.get_right_child)
  end
end


begin
  t =BinaryTree.new(1)
#  t.insert_left(2)
#  t.insert_right(3)
#  t.get_left_child.insert_left(4)
#  t.get_left_child.insert_right(5)
  puts t.inspect
  puts size(t)
end
  
