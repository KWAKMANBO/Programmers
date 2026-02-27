import sys

input = sys.stdin.readline

N, M = map(int, input().split())

num_dict = {}
keys = []

cnt = [0] * 10001
odd_nums_cnt = 0
for i in range(N):
    for n in map(int, input().split()):
        cnt[n] += 1

for c in cnt:
    if c % 2 == 1:
        odd_nums_cnt += 1

y = "YES"
n = "NO"
if M == 1:
    print(y)
elif N < odd_nums_cnt:
    print(n)
elif odd_nums_cnt % 2 == 1 and N % 2 == 0:
    print(n)
elif M % 2 == 0 and odd_nums_cnt != 0:
    print(n)
