from collections import deque


def solution(priorities, location):
    answer = 0
    priorityDict = {i: priorities[i] for i in range(len(priorities))}
    queue = deque([i for i in range(len(priorities))])

    while len(queue) != 0:
        e = queue.popleft()
        if len(queue) == 0:
            return answer + 1
        m = max(priorityDict[q] for q in queue)
        # print(f"e : {e}, m : {m}, queue : {queue}")
        if priorityDict[e] >= m:
            answer += 1
            if e == location:
                return answer
        else:
            queue.append(e)

    return answer