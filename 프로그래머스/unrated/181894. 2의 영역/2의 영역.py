def solution(arr):
    answer = []
    idx = [i for i,value in enumerate(arr) if value == 2]
    
    if len(idx) == 0:
        answer.append(-1)
        return answer
    else:
        return arr[idx[0]: idx[len(idx)-1]+1]
        