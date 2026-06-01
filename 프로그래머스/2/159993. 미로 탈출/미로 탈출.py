from collections import deque


def solution(maps):
    m = len(maps)
    n = len(maps[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    start_node = (0, 0)

    # 시작지점 찾기
    for i in range(m):
        for j in range(n):
            if maps[i][j] == 'S':
                start_node = (i, j)
                break

    def bfs(start_node, cnt, target):
        visited = set()
        queue = deque([(start_node[0], start_node[1], cnt)])
        visited.add(start_node)
        while queue:
            i, j, c = queue.popleft()
            if maps[i][j] == target:
                return i, j, c

            for ii in range(4):

                ni, nj = i + dx[ii], j + dy[ii]

                if 0 <= ni < m and 0 <= nj < n and maps[ni][nj] != 'X' and (ni, nj) not in visited:
                    queue.append((ni, nj, c + 1))
                    visited.add((ni, nj))

        return 0, 0, -1

    r, c, cnt = bfs(start_node, 0, 'L')
    start_node = (r, c)
    if cnt == -1:
        return -1

    answer = bfs(start_node, cnt, 'E')[2]

    return answer