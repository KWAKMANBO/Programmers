def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        tmp = ""
        for w in st:
            if w in skill:
                tmp += w
        if not tmp or (tmp and tmp[0] == skill[0] and tmp in skill):
            answer += 1


    return answer