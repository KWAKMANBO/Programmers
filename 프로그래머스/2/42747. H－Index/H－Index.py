def solution(citations):
    citations.sort()
    answer = 0

    for i in range(1,len(citations)+1):
        cnt = 0
        for j in citations:
            if j >= i:
                break
            else:
                cnt += 1
        if cnt <= i <= len(citations) - cnt:
            answer = i
        else:
            break

    return answer