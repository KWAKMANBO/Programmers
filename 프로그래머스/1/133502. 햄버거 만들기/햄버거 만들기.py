def solution(ingredient):
    answer = 0
    tmp = []
    for i in ingredient:
        tmp.append(i)
        if tmp[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                tmp.pop()

    return answer