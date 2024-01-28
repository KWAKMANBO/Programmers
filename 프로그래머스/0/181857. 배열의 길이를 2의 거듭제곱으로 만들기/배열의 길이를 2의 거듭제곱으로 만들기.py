def solution(arr):
    answer = arr 
    i = 0 
    exp = 0 
    while True:
        exp = 2**i
        if exp < len(arr):
            i += 1
        else:
            break
    
    for i in range(exp - len(arr)):
        answer.append(0)
    return answer