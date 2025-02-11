import sys

n = int(sys.stdin.readline())

people = {}

for _ in range(n):
    p, s = sys.stdin.readline().strip().split()
    people[p] = s

answer = []
for p in people:
    if people[p] == "enter":
        answer.append(p)
answer.sort(reverse= True)

for i in answer:
    print(i)