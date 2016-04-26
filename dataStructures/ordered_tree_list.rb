def tree_to_cll(tree)
  if (tree.nil?)
    return nil
  end
  l1 = tree_to_cll(tree.small)
  l2 = tree_to_cll(tree.large)
  tree.small = tree
  tree.large = tree
  l1 = append(l1, tree)
  return append(l1, l2)
end

def append(a, b)
  if (a.nil?)
    return b
  elsif (b.nil?)
    return a
  end

  join(a.large, b)
  a.small = b
  b.large = a

  return a
end

def join(a,b)
  a.large = b
  b.small = a
end
