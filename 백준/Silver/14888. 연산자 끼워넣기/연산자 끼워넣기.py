import sys


input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

plus, minus, mul, div = map(int, input().split())

maximum = -1000000001
minimum = 1000000001


def dfs(depth, total, plus, minus, mul, div):
    global maximum, minimum
    if depth == N:
        maximum = max(maximum, total)
        minimum = min(minimum, total)
        return

    if plus > 0:
        dfs(depth + 1, total + A[depth], plus - 1, minus, mul, div)
    if minus > 0:
        dfs(depth + 1, total - A[depth], plus, minus - 1, mul, div)
    if mul > 0:
        dfs(depth + 1, total * A[depth], plus, minus, mul - 1, div)
    if div > 0:
        dfs(depth + 1, int(total / A[depth]), plus, minus, mul, div - 1)


dfs(1, A[0], plus, minus, mul, div)

print(maximum)
print(minimum)
