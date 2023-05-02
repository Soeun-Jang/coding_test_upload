def solution(todo_list, finished):
    answer = []
    cnt = 0
    for i in finished:
      if i == False:
        answer.append(cnt)
      cnt += 1
    ans = []
    for i in answer:
      ans.append(todo_list[i])
    
    return ans