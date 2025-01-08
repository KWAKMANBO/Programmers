def solution(s):
    answer = 0
    start = ''
    same_cnt = 0
    not_same_cnt = 0
    for i in s:
        if start == '':
            start = i
            same_cnt += 1
        elif start == i:
            same_cnt += 1
        elif start != i:
            not_same_cnt += 1

        if same_cnt == not_same_cnt:
            answer += 1
            start = ''
    if start != '':
        answer += 1
    return answer