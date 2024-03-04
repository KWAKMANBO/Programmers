def solution(num_list, n):
    answer = []
    while num_list:
        tmp = []
        for i in range(n):
            tmp.append(num_list.pop(0))
        answer.append(tmp)
    return answer