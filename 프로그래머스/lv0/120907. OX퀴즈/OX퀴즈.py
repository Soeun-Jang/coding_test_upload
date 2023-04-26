
div = []
answer = []
def solution(quiz):
    answer = []
    for i in quiz:
        div = i.split(' ')
        if div[1] == '-':
          a = int(div[0]) - int(div[2])
          if a == int(div[4]):
            answer.append("O")
            print(answer)
          else:
            answer.append("X")
            print(answer)
        if div[1] == '+':
          a = int(div[0]) + int(div[2])
          if a == int(div[4]):
            answer.append("O")
            print(answer)
          else:
            answer.append("X")
            print(answer)
    return answer

