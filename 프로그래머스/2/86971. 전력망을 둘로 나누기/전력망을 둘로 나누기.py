from collections import deque


def solution(n, wires):
    answer = 100
    tree = {i: [] for i in range(1, n + 1)}

    for w in wires:
        s, e = w
        tree[s].append(e)
        tree[e].append(s)

    def bfs(start_node, no_visit_node):
        queue = deque()
        queue.append(start_node)
        visited = set()
        visited.add(start_node)
        cnt = 1

        while queue:
            node = queue.popleft()

            for t in tree[node]:
                if t not in visited and t != no_visit_node:
                    visited.add(t)
                    queue.append(t)
                    cnt += 1

        return cnt

    for w in wires:
        s, e = w
        answer = min(answer, abs(bfs(s, e) - bfs(e, s)))

    return answer