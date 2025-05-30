# Input
# 5 8 3
# 2 4 5 4 6

import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[N - 1]
second = data[N - 2]
result = 0

while True:
    for i in range(K):
        if M == 0:
            break
        result += first
        M -= 1
    if M == 0:
        break
    result += second
    M -= 1

print(result)