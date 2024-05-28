import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

basket = [int(i) + 1 for i in range(n)]

for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    basket[a - 1], basket[b - 1] = basket[b - 1], basket[a - 1]

print(*basket)
