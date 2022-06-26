import re
import operator
from rpn import *
from stack import *

def is_number(token):
  return re.fullmatch(r'\d+|\d+\.\d+', token)

def is_operator(token):
  return token in ['+', '-', 'x', '*', '/']

def is_operation(token):
  return token in ['.', '_']

def parse_number(token):
  return float(token)

def primitive_operator(token):
  if token == '+':
    return operator.add
  elif token == '-':
    return operator.sub
  elif token == 'x' or token == '*':
    return operator.mul
  elif token == '/':
    return operator.truediv
  else:
    raise Exception(f'Invalid operator {token} -- PRIMITIVE_OPERATOR')

def process(token, stack):
  if token == '.':
    pop(stack)
  elif token == '_':
    empty(stack)
  else:
    raise Exception(f'Invalid operation {token} -- PROCESS')

def operate(op, n1, n2):
  return op(n1, n2)

def execute(rpn):
  stack = make_stack()

  for token in tokenize(rpn):
    if is_number(token):
      push( parse_number(token), stack )
    elif is_operator(token):
      n2 = pop(stack)
      n1 = pop(stack)
      op = primitive_operator(token)
      push( operate(op, n1, n2), stack )
    elif is_operation(token):
      process(token, stack)
    else:
      raise Exception(f'Invalid token {token} -- EXECUTE')

  return stack_to_rpn(stack)
