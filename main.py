from calculator import *
from driver_loop import *

def sample_tree():
  return make_tree('+',
                   make_tree('+',
                             make_tree('x',
                                       make_leaf('6'),
                                       make_leaf('7')),
                             make_leaf('3')),
                   make_tree('-',
                             make_tree('+',
                                       make_leaf('9'),
                                       make_tree('/',
                                                 make_leaf('6'),
                                                 make_leaf('2'))),
                             make_leaf('2')))

def print_example(input):
  print(f'      {input}')
  print(execute(input))

def safe_execute(rpn):
  try:
    return execute(rpn)
  except Exception as error:
    return(str(error))

if __name__ == '__main__':
  print('RPN CALCULATOR V1.1\n')
  print('In reverse polish notation, operators follow operands.')
  print('To add 3 and 4 together, write 3 4 + rather than 3 + 4.\n')

  print_example( '3 4 +' )
  print_example( '3 4 - 5 x' )

  tree = sample_tree()
  print_example( tree_to_rpn(tree) )

  print()
  print('Enter an expression below to get an answer.')
  print('To end the program, type exit or quit.\n')

  driver_loop(safe_execute)
