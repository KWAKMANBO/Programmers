from collections import Counter
from collections import deque
import sys

sys.setrecursionlimit(10**6)

def solution(edges):
    answer = [0, 0, 0, 0]

    graph = {}

    in_degree = Counter()
    out_degree = Counter()

    state = {}
    for s, e in edges:
        if s not in graph:
            graph[s] = [e]
        else:
            graph[s].append(e)

        if e not in graph:
            graph[e] = []

        if s not in state:
            state[s] = 0
        if e not in state:
            state[e] = 0

        out_degree[s] += 1
        in_degree[e] += 1

    new_node = -1
    for node in out_degree.most_common():
        if in_degree[node[0]] == 0:
            new_node = node[0]
            break
    answer[0] = new_node

    def has_cycle_dfs(node):
        state[node] = 1

        for g in graph[node]:
            if state[g] == 1:
                return True

            if state[g] == 0:
                if has_cycle_dfs(g):
                    return True

        state[node] = 2
        return False

    def calculate_node_and_edge_cnt(node):
        q = deque([node])
        visited = {node}
        node_cnt, edge_cnt = 0, 0
        while q:
            nnode = q.popleft()
            node_cnt += 1
            edge_cnt += out_degree[nnode]
            for next in graph[nnode]:
                if next not in visited:
                    visited.add(next)
                    q.append(next)

        return node_cnt, edge_cnt

    for node in graph[new_node]:

        node_cnt, edge_cnt = calculate_node_and_edge_cnt(node)
        if has_cycle_dfs(node):
            if node_cnt == edge_cnt:
                answer[1] += 1
            else:
                answer[3] += 1
        else:
            answer[2] += 1

    return answer