def solution(data, col, row_begin, row_end):
    answer = 0
    # col기준으로 정렬하기
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    lst = []
    for i in range(row_begin - 1, row_end):
        tmp = 0
        for d in data[i]:
            tmp += d % (i + 1)
        lst.append(tmp)

    answer = lst[0]
    for l in lst[1:]:
        answer = answer ^ l

    return answer