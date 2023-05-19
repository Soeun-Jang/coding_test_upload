def solution(x, n): 
    answer = []
    if x == 0:
        return [0] * n
    elif x < 0:
        return list(range(x,(x*n)-1,x))
    elif x > 0:
        return list(range(x,(x*n)+1,x))