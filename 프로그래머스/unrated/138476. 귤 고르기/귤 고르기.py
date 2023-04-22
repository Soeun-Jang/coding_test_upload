def solution(k, tangerine): # k = 귤의 개수, tangerine = 귤의 크기를 담은 배열
    
    num_list = {}
    for num in tangerine: # num = 1 
        if num not in num_list: 
            num_list[num] = 1
        else:
            num_list[num] += 1


    sorted_num_list = sorted(num_list.items(), key=lambda x: x[1], reverse=True)

    count = 0
    result = 0
    for i in sorted_num_list:    
      count += i[1]
      result += 1
      if count >= k:
        return result
    