class BinaryTree
  attr_accessor :left_child, :right_child

  def initialize(val)
    @val = val
    @left_child = nil
    @right_child = nil
  end

  def insert_left(val)
    current_left = @left_child
    new_left = BinaryTree.new(val)
    @left_child = new_left
    new_left.left_child = current_left
  end

  def insert_right(val)
    current_right = @right_child
    new_right = BinaryTree.new(val)
    @right_child = new_right
    new_right.right_child = current_right
  end

  def get_left_child
    return @left_child
  end

  def get_right_child
    return @right_child
  end

  def set_root_val(val)
    @val = val
  end

  def get_root_val
    return @val
  end

  def inorder
    if (!@left_child.nil?)
      @left_child.inorder
    end
    puts @val
    if (!@right_child.nil?)
      @right_child.inorder
    end
  end

  def postorder
    if (!@left_child.nil?)
      @left_child.postorder
    end
    if (!@right_child.nil?)
      @right_child.inorder
    end
    puts @val
  end

  def preorder
    puts @val
    if (!@left_child.nil?)
      @left_child.postorder
    end
    if (!@right_child.nil?)
      @right_child.inorder
    end
  end

end

class BinarySearchTree

  attr_accessor :left_child, :right_child, :parent, :key, :val

  def initialize(key, val, left=nil, right=nil, parent=nil)
    @key = key
    @val = val
    @left_child = left
    @right_child = right
    @parent = parent
  end

  def insert(key, val)
    if (key == @key)
      @val = val
    elsif (key < @key)
      if (has_left_child?)
        @left_child.insert(key,val)
      else
        @left_child = BinarySearchTree.new(key, val, nil, nil, self)
      end
    else
      if (has_right_child?)
        @right_child.insert(key, val)
      else
        @right_child = BinarySearchTree.new(key, val, nil, nil, self)
      end
    end
  end

  def find(key)
    if (key == @key)
      return @val
    elsif(key < @key)
      if (has_left_child?)
        @left_child.find(key)
      else
        return nil
      end
    else
      if (has_right_child?)
        @right_child.find(key)
      else
        return nil
      end
    end
  end

  def delete(key)
    if (key == @key)
      if (is_leaf?)
        delete_leaf
      elsif (has_both_childs?)
        delete_two_child_node
      else
        delete_one_child_node
      end
    elsif (key < @key)
      if (has_left_child?)
        @left_child.delete(key)
      else
        return nil
      end
    else
      if (has_right_child?)
        @right_child.delete(key)
      else
        return nil
      end
    end
  end

  def delete_leaf
    if (is_left_child?)
      @parent.left_child = nil
    else
      @parent.right_child = nil
    end
  end

  def delete_one_child_node
    if (has_left_child?)
      if (is_left_child?)
        @parent.left_child = @left_child
        @left_child.parent = @parent
      elsif (is_right_child?)
        @parent.right_child = @left_child
        @left_child.parent = @parent
      else
        replace(@left_child)
      end
    else
      if (is_left_child?)
        @parent.left_child = @right_child
        @right_child.parent = parent
      elsif (is_right_child?)
        @parent.right_child = @right_child
        @right_child.parent = parent
      else
        replace(@right_child)
      end
    end
  end

  def replace(tree)
    @key = tree.key
    @val = tree.val
    @left_child = tree.left_child
    @right_child = tree.right_child
    if (has_right_child?)
      @right_child.parent = self
    end
    if (has_left_child?)
      @left_child.parent = self
    end
  end

  def delete_two_child_node
    successor = @right_child.min_child
    successor.splice_out
    @val = successor.val
    @key = successor.key
  end

  def splice_out
    if (is_leaf?)
      if (is_left_child?)
        @parent.left_child = nil
      else
        @parent.right_child = nil
      end
    elsif (has_left_child?)
      if (is_left_child?)
        @parent.left_child = @left_child
      else
        @parent.right_child = @left_child
      end
      @left_child.parent = @parent
    else
      if (is_left_child?)
        @parent.left_child = @right_child
      else
        @parent.right_child = @right_child
      end
      @right_child.parent = @parent
    end
  end

  def min_child
    if (has_left_child?)
      return @left_child.min_child
    else
      return self
    end
  end

  def max_child
    if (has_right_child?)
      return @right_child.max_child
    else
      return self
    end
  end

  def is_left_child?
    return (!@parent.nil? and self == @parent.left_child)
  end

  def is_right_child?
    return (!@parent.nil? and self == @parent.right_child)
  end

  def has_left_child?
    return !@left_child.nil?
  end

  def has_right_child?
    return !@right_child.nil?
  end

  def has_both_childs?
    return (!@left_child.nil? and !@right_child.nil?)
  end

  def is_leaf?
    return (@left_child.nil? and @right_child.nil?)
  end

  def inorder
    if (!@left_child.nil?)
      @left_child.inorder
    end
    puts @key
    if (!@right_child.nil?)
      @right_child.inorder
    end
  end


end

class AVLTree < BinarySearchTree

  attr_accessor :balance

  def initialize(key, val, left=nil, right=nil, parent=nil)
    super(key, val, left, right, parent)
    @balance = 0
  end

  def insert(key, val)
    if (key == @key)
      @val = val
    elsif (key > @val)
      if (has_right_child?)
        @right_child.insert(key, val)
      else
        @right_child = AVLTree.new(key, val)
        @right_child.update_balance
      end
    else
      if (has_left_child?)
        @left_child.insert(key, val)
      else
        @left_child = AVLTree.new(key, val)
        @left_child.update_balance
      end
    end
  end

  def update_balance
    if (@balance < -1 or @balance > 1)
      rebalance
      return
    end
    if (!@parent.nil?)
      if (is_right_child?)
        @parent.balance -= 1
      elsif (is_left_child?)
        @parent.balance += 1
      end

#      if (@parent.balance <> 0)
#        @parent.update_balance
#      end
    end
  end

  def rebalance
    if (@balance > 1) # left heavy, do right rotation
      if (@left_child.balance < 0) # first left rotate left child
        @left_child.left_rotate
      end
      right_rotate
    elsif (@balance < -1) # right heavy, do left rotation
      if (@right_child > 0) # first right rotate right child
        @right_child.right_rotate
      end
      left_rotate
    end
  end

  def right_rotate
    new = @left_child
    new.parent = @parent
    if (is_left_child?)
      @parent.left_child = new
    elsif (is_right_child?)
      @parent.right_Child = new
    end
    if (new.has_right_child?)
      new.right_child.parent = self
      self.left_child = new.right_child
    end
    new.right_child = self
    @parent = new
  end

  def left_rotate
    new = @right_child
    new.parent = @parent
    if (is_left_child?)
      @parent.left_child = new
    elsif (is_right_child?)
      @parent.right_child = new
    end
    if (new.has_left_child?)
      new.left_child.parent = self
      @right_child = new.left_child
    end
    new.left_child = self
    @parent = new
  end

  def get_balance
    if (has_both_children?)
      return @left_child.height - @right_child.height
    elsif (has_right_child?)
      return 0 - @right_child.height
    elsif (has_left_child?)
      return @left_child.height
    else
      return 0
    end
  end

end


def tree_construct_in_pre(inorder, preorder)
  t = BinaryTree.new(preorder.slice(0))
  if (inorder.length <= 1)
    return t
  else
    ind = inorder.index(preorder.slice(0))
    left_substr = inorder.slice(0,ind)
    right_substr = inorder.slice(ind+1, inorder.length)
    preorder.slice!(0)
    t.left_child = tree_construct_in_pre(left_substr, preorder.slice(0,left_substr.length))
    t.right_child = tree_construct_in_pre(right_substr, preorder.slice(left_substr.length, preorder.length)) if preorder.length > 1
    return t
  end
end

def tree_construct_in_post(inorder, postorder)
  t = BinaryTree.new(postorder[postorder.length-1])
  if (inorder.length <= 1)
    return t
  else
    ind = inorder.index(postorder.slice(postorder.length-1))
    left_substr = inorder.slice(0,ind)
    right_substr = inorder.slice(ind+1, inorder.length)
    postorder.slice!(postorder.length-1)
    t.right_child = tree_construct_in_post(right_substr, postorder.slice(left_substr.length, postorder.length)) #if postorder.length > 1
    t.left_child = tree_construct_in_post(left_substr, postorder.slice(0, left_substr.length))
    return t
  end
end



def binary_tree(val)
  return [val,[],[]]
end

def insert_left(root, val)
  current_left = root.slice(1)
  new_left = binary_tree(val)
  new_left[1] = current_left
  root[1] = new_left
  return root
end

def insert_right(root, val)
  current_right = root.slice(2)
  new_right = binary_tree(val)
  new_right[2] = current_right
  root[2] = new_right
  return root
end


def get_root_val(root)
  return root.first
end

def set_root_val(root, val)
  root[0] = val
end

def get_left_child(root)
  return root[1]
end

def get_right_child(root)
  return root[2]
end


def root_node_paths(bin_tree, paths)
  if (leaf?(bin_tree))
    puts (paths + [bin_tree.get_root_val]).to_s
    return paths + [bin_tree.get_root_val]
  else
    tmp1 = paths + root_node_paths(bin_tree.get_left_child, [bin_tree.get_root_val])
    puts tmp1.to_s
    tmp2 = paths + root_node_paths(bin_tree.get_right_child, [bin_tree.get_root_val])
    puts tmp2.to_s
    return [tmp1,tmp2]
#    printf bin_tree.get_root_val.to_s + '->' + print_root_node_paths(bin_tree.get_left_child)
#    printf bin_tree.get_root_val.to_s + '->' + print_root_node_paths(bin_tree.get_right_child)
  end
end

def _print_root_node_paths(bin_tree, paths)
  if (leaf?(bin_tree))
    puts (paths + [bin_tree.get_root_val]).to_s
  else
    _print_root_node_paths(bin_tree.get_left_child, paths + [bin_tree.get_root_val]) if !bin_tree.get_left_child.nil?
    _print_root_node_paths(bin_tree.get_right_child, paths + [bin_tree.get_root_val]) if !bin_tree.get_right_child.nil?
  end
end

def leaf?(node)
  if (node.get_left_child.nil? and node.get_right_child.nil?)
    return true
  else
    return false
  end
end

def find_max(tree)
  if (leaf?(tree))
    return tree.get_root_val
  else
    max_left = if !tree.get_left_child.nil? then find_max(tree.get_left_child) else -1000 end
    max_right = if !tree.get_right_child.nil? then find_max(tree.get_right_child) else -1000 end
    current_val = tree.get_root_val
    if (max_left > current_val and max_left > max_right)
      return max_left
    elsif (max_right > current_val and max_right > max_left)
      return max_right
    else
      return current_val
    end
  end
end


def bst_to_cll(bst)
  if (bst.is_leaf?)
    return bst
  elsif(bst.has_both_children?)
    l1 = bst_to_cll(bst.left_child)
    l2 = bst_to_cll(bst.right_child)
    return append(append(l1, bst), l2)
  elsif(bst.has_left_child?)
    return append(bst_to_cll(bst.left_child, bst))
  else
    return append(bst, bst_to_cll(bst.right_child))
end

def append(left, right)
  left.right_child = right
  right.left_child = left
  left.left_child = right
  right.right_child = left
  return left
end

def ll_walk(head)
  puts head.key.to_s + '->'
  if (head.has_right_child?)
    ll_walk(head.right_child)
  end
end

end
