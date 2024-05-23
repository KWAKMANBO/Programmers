n = int(input())

answer = []
cnt = 0
if n % 5 == 0:
    answer.append(n // 5)
elif n % 3 == 0:
    answer.append(n // 3)

while n > 3:
    n = n - 3
    cnt += 1
    if n % 5 == 0:
        cnt += n // 5
        n %= 5
if n == 0:
    answer.append(cnt)
else:
    if len(answer) == 0:
        answer.append(-1)

print(min(answer))
