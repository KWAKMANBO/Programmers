import sys

input = sys.stdin.readline

a, b = map(int, input().split())

answer = 1

while True:

    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    else:
        break
    answer += 1

    if b <= a:
        break

print(answer if b == a else -1)
