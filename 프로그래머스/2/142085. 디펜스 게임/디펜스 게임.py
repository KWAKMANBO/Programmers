import heapq


def solution(n, k, enemy):
    answer = 0
    q = []

    for e in enemy:
        heapq.heappush(q, -1 * e)

        n -= e

        if n < 0:
            if k > 0:
                n += -1 * heapq.heappop(q)
                k -= 1
            else:
                break

        answer += 1

    return answer