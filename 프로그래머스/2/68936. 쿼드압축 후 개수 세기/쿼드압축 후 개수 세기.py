from collections import deque


def solution(arr):
    answer = [0, 0]
    q = deque()
    q.append((0, 0, len(arr), len(arr)))

    def check(val, si, sj, ei, ej):
        for i in range(si, ei):
            for j in range(sj, ej):
                if arr[i][j] != val:
                    return False
        return True

    while q:
        si, sj, ei, ej = q.popleft()
        val = arr[si][sj]
        if check(val, si, sj, ei, ej):
            if val == 0:
                answer[0] += 1
            else:
                answer[1] += 1
        else:
            q.append((si, sj, si + (ei - si) // 2, sj + (ej - sj) // 2))
            q.append((si, sj + (ej - sj) // 2, si + (ei - si) // 2, ej))
            q.append((si + (ei - si) // 2, sj, ei, sj + (ej - sj) // 2))
            q.append((si + (ei - si) // 2, sj + (ej - sj) // 2, ei, ej))


    return answer
