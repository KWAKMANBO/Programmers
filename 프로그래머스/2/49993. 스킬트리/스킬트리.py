from collections import deque


def solution(skill, skill_trees):
    answer = 0
    order = {i: v for i, v in enumerate(skill)}

    for s in skill_trees:
        q = deque(skill)
        tmp = ""
        for i in s:
            if i in skill:
                tmp += i

        if not tmp or (tmp and tmp[0] == skill[0] and tmp in skill):
            answer += 1

    return answer