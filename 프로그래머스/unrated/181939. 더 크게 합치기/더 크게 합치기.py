
def solution(a, b):
    c = str(a)+str(b)
    d = str(b)+str(a)
    e = int(c)
    f = int(d)
    if e < f:
      return f
    if e > f:
      return e
    else:
      return e
