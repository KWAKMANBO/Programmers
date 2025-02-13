import sys

n, m = map(int, sys.stdin.readline().split())

nset = set()
mset = set()

for i in sys.stdin.readline().split():
    nset.add(i)

for i in sys.stdin.readline().split():
    mset.add(i)

answer = []
for i in nset:
    if i not in mset:
        answer.append(i)

for i in mset:
    if i not in nset:
        answer.append(i)

print(len(answer))
