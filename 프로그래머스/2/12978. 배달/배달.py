import heapq


def solution(N, road, K):
    INF = 500001
    dist = [INF] * (N + 1)

    graph = [[] for _ in range(N + 1)]

    start = 1

    for r in road:
        s, e, l = r
        graph[s].append((e, l))
        graph[e].append((s, l))

    q = []
    heapq.heappush(q, (0, 1))
    dist[1] = 0
    while q:
        length, node = heapq.heappop(q)
        if dist[node] < length:
            continue

        for g in graph[node]:
            cost = length + g[1]
            if cost < dist[g[0]]:
                dist[g[0]] = cost
                heapq.heappush(q, (cost, g[0]))

    answer = 0
    for d in dist:
        if d <= K:
            answer += 1

    return answer