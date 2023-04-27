def solution(dots):
    a = []
    b = []

    for i in range(len(dots)):
        a.append(dots[i][0])
        b.append(dots[i][1])

    m = abs(a[2]-a[3])/abs(a[0]-a[1])  
    print(m)
    n = abs(b[2]-b[3])/abs(b[0]-b[1])
    print(m)

    if m == n:
        return 1
    else:
         return 0
