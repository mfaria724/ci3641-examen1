# implementation of zipWith 
# a and b should be lists and func should be a function
def zipWith(a, b, func):
  if a and b:
    yield func(a[0], b[0])
    for p in zipWith(a[1:], b[1:], func):
      yield p

# execution example
# for p in zipWith([0,1,2,1], [1,2,1,0], lambda x, y: x + y):
#   print(p)
