def solution(elements):
    answer = set()

    #시작점
    for i in range(len(elements)):
        s = 0
        for j in range(i+1, i + len(elements)+1):
            s += elements[j% len(elements)]
            answer.add(s)

    return len(answer)