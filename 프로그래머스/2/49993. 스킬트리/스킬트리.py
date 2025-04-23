from collections import deque


def solution(skill, skill_trees):
    answer = 0

    for st in skill_trees:
        q = deque(skill)
        flag = True
        for w in st:
            if w in q and w == q[0]:
                q.popleft()
            elif w in q and w != q[0]:
                flag = False
                break

        if flag:
            answer += 1

    return answer