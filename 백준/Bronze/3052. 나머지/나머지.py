list = []
for i in range(10):
    num = int(input())
    list.append(num % 42)


cnt = set()
for j in list:
    cnt.add(j)


print(len(cnt))
