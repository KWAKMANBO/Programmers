from collections import deque


def solution(order):
    answer = 0
    tmp_belt = deque([])
    belt = deque([i for i in range(1, len(order) + 1)])
    idx = 0
    while True:
        if belt and belt[0] == order[idx]:
            belt.popleft()
            answer += 1
            idx += 1
        elif tmp_belt and tmp_belt[-1] == order[idx]:
            tmp_belt.pop()
            answer += 1
            idx += 1
        elif belt and belt[0] != order[idx]:
            tmp_belt.append(belt.popleft())
        elif not belt and not tmp_belt:
            break
        else :
            break


    return answer