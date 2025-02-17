def solution(k, tangerine):
    answer = 0
    tangerineCnt = {}
    for t in tangerine:
        if t not in tangerineCnt:
            tangerineCnt[t] = 1
        else:
            tangerineCnt[t] += 1

    lst = list(tangerineCnt.values())
    lst.sort(reverse=True)
    cnt = 0
    for i in range(len(lst)):
        cnt += lst[i]
        answer +=1
        if cnt >= k:
            return answer