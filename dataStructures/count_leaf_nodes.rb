require_relative 'binTree'

def count_leaf_nodes(tree)
  if (tree.nil?)
    return 0
  else
    if (tree.get_left_child.nil? and tree.get_right_child.nil?)
      # is a leaf node, so return 1
      return 1
    else
      return count_leaf_nodes(tree.get_left_child) + count_leaf_nodes(tree.get_right_child)
    end
  end
end


begin
  t = BinaryTree.new(1)
  t.insert_left(2)
  t.insert_right(0)
  t.get_left_child.insert_left(3)
  t.get_left_child.insert_right(4)
  t.get_right_child.insert_right(8)
  puts t.inspect
  puts count_leaf_nodes(t)
end
