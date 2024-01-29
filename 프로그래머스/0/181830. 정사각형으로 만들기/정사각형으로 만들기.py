def solution(arr):
    answer = arr
    row = len(arr)
    col = len(arr[0])
    
    if row < col:
        for i in range(col - row):
            answer.append([0 for j in range(len(arr[0]))])
    if row > col :
        for i in range(len(answer)):
            for j in range(row - col):
                answer[i].append(0)
            
    return answer