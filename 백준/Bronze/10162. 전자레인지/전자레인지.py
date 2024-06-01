import sys

t = int(sys.stdin.readline().rstrip())

lst = [300, 60, 10]
answer = []

for i in lst:
    answer.append(t // i)
    t %= i

if t != 0:
    print(-1)
else:
    print(*answer)
