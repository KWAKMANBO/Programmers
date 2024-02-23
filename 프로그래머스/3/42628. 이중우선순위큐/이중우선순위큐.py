def solution(operations):
    answer = []
    for i in operations:
        tmp = i.split()
        if tmp[0] == 'I':
            answer.append(int(tmp[1]))
            answer.sort()
        if tmp[0] == 'D':
            if len(answer) == 0:
                continue
            if tmp[1] == '-1':
                answer.pop(0)
            elif tmp[1] == "1":
                answer.pop()

    if len(answer) == 0:
        return [0,0]

    return [max(answer), min(answer)]