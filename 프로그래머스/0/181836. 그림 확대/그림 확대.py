def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        tmp = []
        for j in range(len(picture[i])):
            tmp.append(picture[i][j]*k)

        for _ in range(k):
            answer.append("".join(tmp))
    return answer