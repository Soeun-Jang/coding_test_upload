def solution(s): # "Zbcdefg"
    answer = []
    arr = []
    for i in s:
        answer.append(ord(i))
    answer.sort(reverse=True)
    for j in answer:
        arr.append(chr(j))
    
    
    return ''.join(arr)