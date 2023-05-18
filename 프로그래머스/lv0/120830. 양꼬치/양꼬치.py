def solution(n, k): #n:양꼬치, k:음료개수 
    answer = 0
    c = list(range(0,n+1,10))
    print(c,len(c))
    a = n * 12000
    b = (k * 2000) - ((len(c)-1)*2000)

    answer = a+b
    
    return answer