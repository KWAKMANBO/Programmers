import sys

n = int(sys.stdin.readline())

coins = [25, 10, 5, 1]
answer = []

for _ in range(n):
    m = int(sys.stdin.readline().rstrip())
    tmp = []
    for i in coins:
        tmp.append(m // i)
        m %= i
    answer.append(tmp)

for i in answer:
    print(*i)
