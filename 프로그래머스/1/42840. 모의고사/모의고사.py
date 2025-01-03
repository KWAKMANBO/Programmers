def solution(answers):
    answer = [0, 0, 0]
    spj = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for i in range(len(answers)):
        if spj[0][i % 5] == answers[i]:
            answer[0] += 1
        if spj[1][i % 8] == answers[i]:
            answer[1] += 1
        if spj[2][i % 10] == answers[i]:
            answer[2] += 1
    result = []
    for i in range(len(answer)):
        if answer[i] == max(answer):
            result.append(i + 1)
    return result
