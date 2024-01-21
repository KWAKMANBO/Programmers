def solution(arr, n):
    answer = []
    if len(arr) % 2 == 1:
        for i, value in enumerate(arr):
            if (i + 1) % 2 == 1:
                answer.append(value + n)
            else:
                answer.append(value)
    else:
        for i, value in enumerate(arr):
            if (i+1) % 2 == 0 :
                answer.append(value + n)
            else:
                answer.append(value)
            
    return answer