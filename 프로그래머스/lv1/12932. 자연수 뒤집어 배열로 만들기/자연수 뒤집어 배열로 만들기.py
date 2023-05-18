def solution(n): #12345
    answer = []
    a = list(str(n))
    a.reverse()
    for i in a:
        answer.append(int(i))
    
    
    return answer