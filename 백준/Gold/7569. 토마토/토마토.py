import sys
from collections import deque

input = sys.stdin.readline

# M : 가로 N : 세로  H : 높이
M, N, H = map(int, input().split())

dh = [-1, 1, 0, 0, 0, 0]
dn = [0, 0, -1, 1, 0, 0]
dm = [0, 0, 0, 0, -1, 1]

arr = []
for _ in range(H):
    tmp = []
    for _ in range(N):
        tmp.append(list(map(int, input().split())))
    arr.append(tmp)


def bfs():
    global arr

    q = deque()

    for h in range(H):
        for n in range(N):
            for m in range(M):
                if arr[h][n][m] == 1:
                    q.append((h, n, m, 0))

    ans = 0
    while q:
        sh, sn, sm, day = q.popleft()
        ans = max(ans, day)
        for i in range(6):
            nh, nn, nm = sh + dh[i], sn + dn[i], sm + dm[i]
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and arr[nh][nn][nm] == 0:
                arr[nh][nn][nm] = 1
                q.append((nh, nn, nm, day + 1))

    for h in range(H):
        for n in range(N):
            for m in range(M):
                if arr[h][n][m] == 0:
                    return -1
    
    return ans


print(bfs())
