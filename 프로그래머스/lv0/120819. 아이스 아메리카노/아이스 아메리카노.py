def solution(money): #5500
    list = []
    americano = 5500
    answer = money//5500
    amount = money%5500
    list.append(answer)
    list.append(amount)
    
    return list