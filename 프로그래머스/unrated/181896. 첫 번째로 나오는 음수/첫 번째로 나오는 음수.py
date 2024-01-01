def solution(num_list):
    idx = -1
    for i in range(len(num_list)):
        if num_list[i] < 0:
            idx = i
            break
        
    return idx