def solution(k, m, score):
    answer = []
    score.sort(reverse=True)
    for i in range(len(score) // m):
        answer.append(min(score[i * m: i * m + m])*m)
    return sum(answer)
