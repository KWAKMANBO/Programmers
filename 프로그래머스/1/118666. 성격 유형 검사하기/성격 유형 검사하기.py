def solution(survey, choices):
    answer = ''
    scores = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    chs = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    type = ['RT', 'CF', 'JM', 'AN']
    for i in range(len(survey)):
        if choices[i] < 4:
            chs[survey[i][0]] += scores[choices[i]]
        elif choices[i] > 4:
            chs[survey[i][1]] += scores[choices[i]]

    for t in type:
        if chs[t[0]] >= chs[t[1]]:
            answer += t[0]
        else:
            answer += t[1]

    return answer