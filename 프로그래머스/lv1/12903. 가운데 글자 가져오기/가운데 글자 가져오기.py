def solution(s): #"abcde"
    answer = ''
    if len(s)%2 == 1:
        return s[len(s)//2]
    else:
        return s[(len(s)//2)-1:(len(s)//2)+1]
    
    return answer