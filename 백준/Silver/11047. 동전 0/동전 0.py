n, k = map(int, input().split())

coin_list = []
answer = 0

for _ in range(n):
    coin_list.append(int(input()))

coin_list = coin_list[::-1]

for i in coin_list:
    if k >= i:
        answer += k // i
        k %= i

print(answer)
