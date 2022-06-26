import sys

def match(s1, s2):
  return str.lower(s1) == str.lower(s2)

def match_any(keywords, s):
  return any( map( lambda k: match(k, s), keywords ) )

def driver_loop(interact):
  prompt()

  for line in sys.stdin:
    input  = line.strip()

    if match_any(['exit', 'quit'], input):
      break

    output = interact(input)

    if len(input) == 0 or len(output) == 0:
      prompt()
    else:
      print(output)
      prompt()

def prompt():
  print('      ', end='', flush=True)
