def solution(N, stages):
    answer = []
    stage_info = [0 for _ in range(N + 1)]

    for i in stages:
        stage_info[i - 1] += 1

    for i in range(len(stage_info)):
        c = sum(stage_info[i:])
        if c == 0 :
            answer.append(0)
        else:
            answer.append(stage_info[i] / sum(stage_info[i:]))
    result = []
    answer = answer[:-1]

    for _ in range(len(answer)):
        result.append(answer.index(max(answer)) + 1)
        answer[answer.index(max(answer))] = -1

    return result


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
