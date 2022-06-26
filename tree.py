def make_tree(entry, left, right):
  return (entry, left, right)

def entry(tree):
  return tree[0]

def left_branch(tree):
  return tree[1]

def right_branch(tree):
  return tree[2]

def make_leaf(entry):
  return make_tree(entry, None, None)

def leaf_node(tree):
  return left_branch(tree) == None and right_branch(tree) == None
