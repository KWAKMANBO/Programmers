answer = 0

def dfs(dungeons, cnt, k, visited):
    global answer
    answer = max(answer, cnt)

    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(dungeons, cnt + 1, k - dungeons[i][1], visited)
            visited[i] = False


def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    dfs(dungeons, 0, k, visited)
    return answer
