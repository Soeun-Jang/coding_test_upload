def solution(num_list, n):
    answer = 0
    for i in num_list:
        if n in num_list:
            return 1
        else:
            return answer