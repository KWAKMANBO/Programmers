def solution(arr, queries):
    answer = []
    for a,b,c in queries:
        # tmp값을 정의
        tmp = -1
        list = []
        for i in range(a,b+1):
            if(arr[i] > c):
                list.append(arr[i])
        if len(list) == 0:
            answer.append(-1)
        else:
            answer.append(min(list))
        
    return answer