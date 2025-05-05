import math
import sys
from difflib import Match

input = sys.stdin.readline

# N은 끊어진 줄의 개수
# M은 주어질 브랜드의 개수
N, M = map(int, input().split())

answer = 0
packages = []
eachs = []
for _ in range(M):
    p, e = map(int, input().split())
    packages.append(p)
    eachs.append(e)
packages.sort()
eachs.sort()

answer = min(math.ceil(N / 6) * packages[0], eachs[0] * N, (N // 6) * packages[0] + (N % 6) * eachs[0])
print(answer)
