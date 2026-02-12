import sys

input = sys.stdin.readline

N = int(input())

felindromes = []
cnt = 0
for _ in range(N):
    tmp = input().strip()
    if tmp == tmp[::-1]:
        cnt +=1

print(cnt * (cnt- 1))
