def solution(before, after):
    answer = 0
    for i in before:
        if before.count(i) != after.count(i) :
            return 0
    return 1