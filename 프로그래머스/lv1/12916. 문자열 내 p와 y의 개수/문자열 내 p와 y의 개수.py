def solution(s):
    answer = True
    cnt1 = 0
    cnt2 = 0
    for i in s:
        if i == "y" or i == "Y":
            cnt1 += 1
        elif i == "p" or i == "P":
            cnt2 += 1
    if cnt1 == cnt2:
        return True
    else: 
        return False
