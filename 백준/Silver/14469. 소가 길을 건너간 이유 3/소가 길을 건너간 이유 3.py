n = int(input())

cow = []
dp = [0] * (n + 1)

for i in range(n):
    cow.append(list(map(int, input().split())))

cow.sort(key=lambda x: x[0])

answer = 0
for c in cow:
    if answer <= c[0]:
        answer = c[0]

    answer += c[1]

print(answer)
