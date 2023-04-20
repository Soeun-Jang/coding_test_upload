def solve_key(skip_list, _char, index): #문자열을 다섯개더할지 일곱개더할지..
  n = 0
  _char = ord(_char)
  while True:
    _char += 1
    if _char > 122:
        _char -= 26
    if _char not in skip_list:
      n += 1
    if n == index:
      break

  return chr(_char)
def solution(s, skip, index):
    skip_list = list(map(lambda x: ord(x), skip))
    s_list = list(map(lambda x: solve_key(skip_list, x,index), s))
    answer = ''.join(s_list)
    return answer