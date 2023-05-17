def solution(n, numlist): #n=5, [1,9,3,10,13,5]
    answer = []
    for i in numlist:
        if i%n ==0:
            answer.append(i)
    
    
    return answer