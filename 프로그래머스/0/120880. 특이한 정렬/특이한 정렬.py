def solution(numlist, n):
    if min(numlist) > n:
        numlist.sort()
        return numlist
    
    if max(numlist) < n:
        numlist.sort()
        numlist.reverse()
        return numlist
    
    answer = []
    idx = 0
    
    
    numlist.sort()
    # n의 경계를 나누는 index찾기
    for i in range(len(numlist)):
        if numlist[i] >= n:
            idx = i
            break
    
    # n보다 작은 배열
    small = numlist[:idx]
    small.reverse()
    # n보다 큰 배열
    up = numlist[idx:] 
    
    for i in range(len(numlist)):
        if len(small) == 0:
            break
        elif len(up) == 0:
            break
        else:
            if n - small[0] == up[0] - n:
                answer.append(up.pop(0))
                answer.append(small.pop(0))
            elif n - small[0] > up[0] - n:
                answer.append(up.pop(0))
            else:
                answer.append(small.pop(0))
    
    if len(small) != 0:
            answer.extend(small)
    elif len(up) != 0:
            answer.extend(up)
    
    return answer