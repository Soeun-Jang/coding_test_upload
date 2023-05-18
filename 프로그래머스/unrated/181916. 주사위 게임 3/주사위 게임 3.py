def solution(a, b, c, d):
    arr = [a,b,c,d]
    dic = {str(i):[0,i] for i in range(1,7)}
    for i in arr:
        dic[str(i)][0]+=1
    print(dic)
    arr2 = sorted(list(dic.values()), reverse=True)
    print(arr2)

    if arr2[0][0] == 4:
        return 1111 * arr2[0][1]
    elif arr2[0][0] == 3:
        return(10*(arr2[0][1]) + arr2[1][1])**2
    elif arr2[0][0] == 2 and arr2[1][0] == 2:
        return (arr2[0][1]+arr2[1][1]) * abs(arr2[0][1] - arr2[1][1])
    elif arr2[0][0] == 2:
        return arr2[1][1]*arr2[2][1]    

    else:
        return arr2[3][1]
