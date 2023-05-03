def solution(n):
    answer = 0
    even = n%2 
    if even == 0:
        for i in range(n):
            if (i+1)%2 == 0:
                answer += (i+1)**2
    if even == 1:
        for i in range(n):
            if (i+1)%2 == 1:
                answer += i+1
    return answer