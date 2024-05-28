import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

basket = [0 for _ in range(n)]

for _ in range(k):
    s, e, b = map(int, sys.stdin.readline().rstrip().split())
    for i in range(s - 1, e):
        basket[i] = b

print(*basket)
