def make_stack():
  return []

def entries(stack):
  return stack.copy()

def push(entry, stack):
  stack.append(entry)

def pop(stack):
  try:
    return stack.pop()
  except Exception:
    raise Exception(f'Stack empty -- POP')

def empty(stack):
  stack.clear()
