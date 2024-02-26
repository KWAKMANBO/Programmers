def solution(array):
    answer =  0
    set_arr = set(array)
    max_cnt = 0
    max_cnt2 = 0
    for i in set_arr:
        cnt = array.count(i)
        if cnt > max_cnt:
            max_cnt = cnt
            answer = i
        elif cnt == max_cnt:
            max_cnt2 = cnt
            
    if max_cnt == max_cnt2:
        return -1
    
    return answer