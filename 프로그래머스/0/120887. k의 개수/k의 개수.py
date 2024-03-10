def solution(i, j, k):
    answer = 0
    arr = [str(i) for i in range(i,j+1)]
    for i in arr:
        if str(k) in i:
            answer += i.count(str(k)) 
    return answer