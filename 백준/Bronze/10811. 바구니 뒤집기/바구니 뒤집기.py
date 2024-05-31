import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

answer = [i for i in range(1, n + 1)]

for _ in range(m):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    s -= 1
    tmp = answer[s:e]
    tmp.reverse()
    answer[s:e] = tmp

print(*answer)