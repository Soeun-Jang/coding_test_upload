def solution(my_string, is_suffix): 
    answer = []
    answer.append(my_string)
    for i in range(len(my_string)):
        answer.append(my_string[i+1:])
    print(answer)

    if is_suffix in answer:
        return 1
    else:
        return 0
    