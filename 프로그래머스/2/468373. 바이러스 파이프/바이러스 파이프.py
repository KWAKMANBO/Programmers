from collections import deque


def solution(n, infection, edges, k):
    answer = 0
    graph = {}
    for e in edges:
        s, e, t = e
        if s not in graph:
            graph[s] = [(e, t)]
        else:
            graph[s].append((e, t))

        if e not in graph:
            graph[e] = [(s, t)]
        else:
            graph[e].append((s, t))

    # 조합을 탐색
    combinations = []

    def dfs(comb, depth, k):
        if depth == k:
            combinations.append(comb)
            return

        for i in range(1,4):
            comb.append(i)
            dfs(comb[:], depth + 1, k)
            comb.pop()

    dfs([], 0, k)

    def bfs(infection_lst, typ):
        q = deque(infection_lst)
        visited = set(infection_lst)

        while q:
            n = q.popleft()
            for g in graph[n]:
                if g[1] == typ and g[0] not in visited:
                    q.append(g[0])
                    infection_lst.append(g[0])
                    visited.add(g[0])

        return infection_lst

    for c in combinations:
        tmp = [infection]

        for i in c:
            tmp = bfs(tmp, i)
        answer = max(answer,len(tmp))

    return answer