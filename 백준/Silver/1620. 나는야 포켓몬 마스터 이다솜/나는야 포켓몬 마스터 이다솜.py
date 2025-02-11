import sys

answer = []
n, m = map(int,sys.stdin.readline().split())

nametonum = {}
numtoname = {}

for i in range(n):
    s = sys.stdin.readline().strip()
    nametonum[s] = i + 1
    numtoname[i + 1] = s

for i in range(m):
    q = sys.stdin.readline().strip()
    if q.isdigit():
        answer.append(numtoname[int(q)])
    else:
        answer.append(nametonum[q])

for i in answer:
    print(i)