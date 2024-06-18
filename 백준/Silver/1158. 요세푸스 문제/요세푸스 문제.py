import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

lst = [i for i in range(1, N + 1)]
idx = 0
answer = []
for i in range(N):
    idx += K - 1

    if idx >= len(lst):
        idx %= len(lst)

    answer.append(str(lst.pop(idx)))

print("<" + ", ".join(answer) + ">")
