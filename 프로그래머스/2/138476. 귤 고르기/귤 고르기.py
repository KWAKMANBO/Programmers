from collections import Counter

def solution(k, tangerine):
    answer = 0
    cnt =0

    cntLst = Counter(tangerine)
    cntLst = cntLst.most_common()

    for c in cntLst:
        cnt += c[1]
        answer +=1
        if cnt >= k :
            return answer