import itertools

def solution(number):
    count = 0
    for i in itertools.combinations(number,3):
        if sum(i) == 0:
            count +=1


    return count