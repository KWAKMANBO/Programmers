def solution(s):
    arr =s.split()
    sum = 0
    for i in range(len(arr)):
        if arr[i] != 'Z':
            sum += int(arr[i])
        else:
            sum -= int(arr[i-1])
            
    return sum