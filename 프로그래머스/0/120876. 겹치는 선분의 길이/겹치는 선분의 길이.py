def solution(lines):
    answer= 0
    arr = [set(range(min(i), max(i))) for i in lines]
    
    return len((arr[0]&arr[1])|(arr[1]&arr[2])|(arr[0]&arr[2]))