import sys

input = sys.stdin.readline

n = int(input())
answer = 0
while n != 0:
    if  n < 0 :
        answer = -1
        break

    if n % 5 == 0:
        answer += n // 5
        n %= 5
    else:
        n -= 2
        answer += 1

print(answer)
