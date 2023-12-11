# 파이썬에서는 swap함수 말고 a,b = b,a 형식으로 교환 가능

def solution(arr, queries):
    
    for i in range(len(queries)):
        arr[queries[i][0]] , arr[queries[i][1]] = arr[queries[i][1]],arr[queries[i][0]] 
    return arr