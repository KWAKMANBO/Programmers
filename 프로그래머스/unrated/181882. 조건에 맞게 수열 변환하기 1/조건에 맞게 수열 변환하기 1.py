def solution(arr):
    answer = []
    for i in arr:
        if i >= 50 and i % 2 == 0:
            answer.append(i/2)
        elif i >= 50  and  i %2 == 1:
            answer.append(i)
        elif i < 50 and  i % 2 == 0:
            answer.append(i)
        else:
            answer.append(i*2)
            
    return answer