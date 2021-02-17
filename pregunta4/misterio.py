from zip import zipWith
import sys

# misterio iterator
def misterio(p):
  yield p
  acum = []
  for p in zipWith([0, *p], [*p, 0], lambda x, y: x + y):
    acum +=[p]
  for m in misterio(acum):
    yield m

# get elements from the misterio iterator and return 
# all of them one by one
def suspenso(p):
  for t in misterio(p):   
    for x in t:
      yield x

c = 0
for m in suspenso([1]):
  # this is an utility to stop at the 7th element
  if c == 28:
    sys.exit()
  else:
    c += 1
  print(m)