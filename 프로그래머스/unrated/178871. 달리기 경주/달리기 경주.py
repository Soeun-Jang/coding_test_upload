def solution(players, callings):
    players_dict = {}
    reverse_dict = {}
    for idx, i in enumerate(players):
        players_dict[i] = idx
        reverse_dict[idx] = i 
    for call in callings:
        p_idx = players_dict[call]
        r_idx = p_idx-1
        r_value = reverse_dict[r_idx] 
        p_value = call
        players_dict[r_value] += 1
        players_dict[p_value] -= 1
        reverse_dict[p_idx] = r_value
        reverse_dict[r_idx] = p_value  

    a = sorted(players_dict.items(), key=lambda x: x[1], reverse=False)
    answer = []
    for i in a:
        answer.append(i[0])

    return answer