import sys

input = sys.stdin.readline

N = int(input())

dp_c1 = [0] * 41
dp_c1[1] = 1
dp_c1[2] = 1
dp_c1[3] = 2
dp_c1[4] = 3

dp_c2 = [0] * 41
dp_c2[3] = 1
dp_c2[4] = 2

for i in range(5, N + 1):
    dp_c1[i] = dp_c1[i - 1] + dp_c1[i - 2]
    dp_c2[i] = i - 2

print(dp_c1[N], dp_c2[N])
