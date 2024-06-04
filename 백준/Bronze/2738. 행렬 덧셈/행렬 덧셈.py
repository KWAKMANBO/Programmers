import sys

n1, n2 = map(int, sys.stdin.readline().rstrip().split())

m = [[], []]
answer = []

for i in range(2):
    for _ in range(n1):
        m[i].append(list(map(int,sys.stdin.readline().rstrip().split())))

for i in range(n1):
    tmp = []
    for j in range(n2):
        tmp.append(m[0][i][j] + m[1][i][j])
    answer.append(tmp)

for i in answer:
    print(*i)