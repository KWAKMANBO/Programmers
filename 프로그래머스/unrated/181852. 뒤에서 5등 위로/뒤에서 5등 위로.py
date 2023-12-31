def solution(num_list):
    answer = num_list
    answer.sort()
    
    for i in range(5):
        answer.pop(0)
    return answer