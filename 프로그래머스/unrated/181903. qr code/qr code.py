def solution(q, r, code): #q=3, r=1, c
    answer = ''
    
    for i,v in enumerate(code):
        if i%q == r:
            answer += v 
    
    
    
    return answer