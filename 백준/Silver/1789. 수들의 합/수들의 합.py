n = int(input())
i = 0
answer = 0
while n >= 0:
    i += 1
    n -= i
    answer += 1

print(answer - 1)
