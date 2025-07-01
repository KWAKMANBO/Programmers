import sys

input = sys.stdin.readline

N, M = map(int, input().split())
pwd = {}
for _ in range(N):
    n, p = input().strip().split()
    pwd[n] = p

for _ in range(M):
    n = input().strip()
    print(pwd[n])
