def solution(my_string):
    numbers = []
    operators = []

    # 숫자와 연산자 분리
    parts = my_string.split()
    for part in parts:
        if part.isdigit():
            numbers.append(int(part))
        else:
            operators.append(part)

    result = numbers[0]  # 첫 번째 숫자를 초기값으로 설정

    # 숫자와 연산자를 순서대로 처리하여 계산
    for i in range(1, len(numbers)):
        operator = operators[i - 1]
        num = numbers[i]
        if operator == '+':
            result += num
        elif operator == '-':
            result -= num

    return result