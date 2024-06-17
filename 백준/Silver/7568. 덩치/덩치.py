import sys

n = int(sys.stdin.readline().rstrip())

lst = []
answer = []
for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(n):
    tmp = 0
    for j in range(n):
        if i == j:
            continue
        else:
            if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
                tmp += 1
    answer.append(tmp + 1)

print(*answer)
