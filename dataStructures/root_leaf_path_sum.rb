require_relative 'binTree'

def root_leaf_path_sum(bst, sum)
  return _root_leaf_path_sum(bst, sum, 0)
end

def _root_leaf_path_sum(bst, sum, current_sum)
  if (bst.nil?)
    return current_sum == sum
  else
    if(_root_leaf_path_sum(bst.left_child, sum, current_sum + bst.get_root_val))
      return true
    elsif(_root_leaf_path_sum(bst.right_child, sum, current_sum + bst.get_root_val))
      return true
    else
      return false
    end
  end
end


bst = BinaryTree.new(10)
bst.insert_left(8)
bst.insert_right(2)
bst.left_child.insert_left(3)
bst.left_child.insert_right(5)
bst.right_child.insert_right(2)
puts root_leaf_path_sum(bst, 18)

