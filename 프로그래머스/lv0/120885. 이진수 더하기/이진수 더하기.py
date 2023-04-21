def _result(bin1, bin2):
  sum1 = _sum(bin1)
    
  sum2 = _sum(bin2)
  return sum1+sum2

def _sum(bin1):
  sum1 = 0
  cnt = 0
  for i in reversed(list(bin1)):
    if i == "1":
      sum1 += 2 ** cnt
    cnt += 1
  return sum1


def solution(bin1, bin2):
    a = _result(bin1,bin2)
    bin_list = []

    while True:
      bin_list.insert(0,a % 2)
      a //= 2
      if a <= 0:
        break
    num_str = ''.join(map(str,bin_list))
    return num_str