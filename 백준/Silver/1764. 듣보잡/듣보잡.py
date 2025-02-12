import sys

# n : 듣도 보도 못한 사람의 수
# m : 보도 못한 사람의 수

n, m = map(int, sys.stdin.readline().split())

bd = {}
db = {}

for i in range(n):
    bd[sys.stdin.readline().strip()] = 1
answer = 0
names = []
for i in range(m):
    name = sys.stdin.readline().strip()
    if bd.get(name):
        answer += 1
        names.append(name)

names.sort()
print(answer)
for i in names:
    print(i)