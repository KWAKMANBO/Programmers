lst = [i for i in range(1, 10001)]

for i in range(1, 10001):
    tmp = i
    for j in str(i):
        tmp += int(j)

    if tmp in lst:
        lst.remove(tmp)

for i in lst:
    print(i)
