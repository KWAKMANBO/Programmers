def solution(t, p):
    answer = 0
    arr = []
    p_len = len(p)
    int_p = int(p)
    for i in range(0, len(t) - p_len+1):
        if int(t[i:i + p_len]) <= int_p:
            answer += 1
    return answer