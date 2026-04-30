from collections import deque


def solution(queue1, queue2):
    answer = 0
    s1 = sum(queue1)
    s2 = sum(queue2)
    sumq = s1 + s2

    q1 = deque(queue1)
    q2 = deque(queue2)
    lq = len(q1) + len(q2)
    if sumq % 2 == 1:
        return -1

    while answer < lq * 3:
        if s1 > s2:
            tmp = q1.popleft()
            q2.append(tmp)
            s1 -= tmp
            s2 += tmp
        elif s1 < s2:
            tmp =  q2.popleft()
            q1.append(tmp)
            s1 += tmp
            s2 -= tmp
        else:
            return answer
        answer += 1
    return -1