import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

q = deque([(0, 0)])
visited = [[0] * N for _ in range(N)]
visited[0][0] = 1

flag = False

while q:
    ci, cj = q.popleft()
    move = arr[ci][cj]

    for di, dj in ((1 * move, 0), (0, 1 * move)):
        ni, nj = ci +di, cj + dj
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            if (ni, nj) == (N - 1, N - 1):
                flag = True
            q.append((ni, nj))


if flag:
    print("HaruHaru")
else:
    print("Hing")
