def solution(arr, k):
    answer = arr
    if k % 2 == 1:
        for i in range(len(answer)):
            answer[i] = answer[i]*k
    else:
        for i in range(len(answer)):
            answer[i] += k
                
    return answer