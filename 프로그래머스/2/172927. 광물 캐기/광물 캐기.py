def solution(picks, minerals):
    answer = 0
    length = min(len(minerals), sum(picks) * 5)
    lst = []
    dia, iron, stone = picks
    for i in range(0, length, 5):
        m = minerals[i:i + 5] 
        tmp = []
        tmp.append(m.count("diamond"))
        tmp.append(m.count("iron"))
        tmp.append(m.count("stone"))
        lst.append(tmp)
    lst.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)

    # 다이아몬드 계산
    for m in lst:
        if dia:
            dia -= 1
            answer += sum(m)
        elif iron:
            iron -= 1
            answer += m[0] * 5 + m[1] + m[2]
        elif stone:
            stone -= 1
            answer += m[0] * 25 + m[1] * 5 + m[2]

    return answer