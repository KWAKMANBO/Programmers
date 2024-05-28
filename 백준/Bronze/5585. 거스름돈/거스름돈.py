import sys

money = 1000 - int(sys.stdin.readline().rstrip())

coins = [500, 100, 50, 10, 5, 1]

answer = 0

for i in coins:
    if money >= i:
        answer += money // i
        money %= i

print(answer)
