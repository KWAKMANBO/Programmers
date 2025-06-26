from collections import deque


def solution(x, y, n):
    queue = deque()
    queue.append((y, 0))
    while queue:
        tmp, cnt = queue.popleft()
        if tmp == x:
            return cnt
            break

        if tmp > x:
            if tmp % 2 == 0:
                queue.append((tmp // 2, cnt + 1))
            if tmp % 3 == 0:
                queue.append((tmp // 3, cnt + 1))
            if tmp - n >=x:
                queue.append((tmp - n, cnt + 1))
    return -1