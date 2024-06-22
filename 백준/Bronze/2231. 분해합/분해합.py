n = int(input())

for i in range(1, n+1):
    tmp = i
    for s in str(i):
        tmp += int(s)

    if tmp == n:
        print(i)
        break
    elif i == n:
        print(0)

