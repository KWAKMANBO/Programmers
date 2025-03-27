def solution(topping):
    l = {}
    r = {}

    answer = 0

    # l 에 모든 토핑 갯수를 저장해서 넣어두기
    for i in topping:
        if i in l:
            l[i] += 1
        else:
            l[i] = 1

    for i in range(len(topping)):
        if topping[i] in r:
            r[topping[i]] += 1
        else:
            r[topping[i]] = 1

        l[topping[i]] -= 1

        if l[topping[i]] == 0:
            del (l[topping[i]])

        if len(l) == len(r):
            answer += 1

    return answer