# input1
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

from collections import deque
import sys

input = sys.stdin.readline

# 최소칸 -> BFS를 사용하기

N, M = map(int, input().split())

board = [list(map(int, input().strip())) for _ in range(N)]

# 시작 지점과 움직인 횟수를 튜플로 등록
queue = deque([(0, 0, 1)])
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y, cnt = queue.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            # 이동할 수 있는 길이며 방문한 적이 없다면?
            if board[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx, ny, cnt + 1))
                visited[nx][ny] = cnt + 1
    if visited[N-1][M-1] != 0:
        print(visited[N - 1][M - 1])
        break


