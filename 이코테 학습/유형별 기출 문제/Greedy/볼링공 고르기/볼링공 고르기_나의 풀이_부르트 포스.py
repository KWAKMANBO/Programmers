# Input1
# 5 3
# 1 3 2 3 2

#Input2
# 8 5
# 1 5 4 3 2 4 5 2

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

lst = list(map(int, input().split()))

answer = 0

for i in range(n - 1):
    for j in range(i+1, n):
        if lst[i] != lst[j]:
            answer += 1

print(answer)
