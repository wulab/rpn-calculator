from tree import *

def make_rpn(*entries):
  def is_integer(number):
    return type(number) == int or number.is_integer()

  def simplify(number):
    if type(number) == float and is_integer(number):
      return int(number)
    elif type(number) == float:
      return round(number, 2)
    else:
      return number

  return str.join('  ', map(str, map(simplify, entries)))

def tokenize(rpn):
  return rpn.split()

def tree_to_rpn(tree):
  if leaf_node(tree):
    return entry(tree)
  else:
    return make_rpn(tree_to_rpn(left_branch(tree)),
                    tree_to_rpn(right_branch(tree)),
                    entry(tree))

def stack_to_rpn(stack):
  return make_rpn(*stack)
