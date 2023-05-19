def solution(n): #118372
    answer = []
    arr = list(str(n))
    for i in arr:
        answer.append(i)
    
    answer.sort(reverse=True)
    print(answer)
    ans = ""
    for i in answer:
        ans += i
    
    return int(ans)