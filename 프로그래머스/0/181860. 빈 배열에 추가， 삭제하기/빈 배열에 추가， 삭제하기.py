def solution(arr, flag):
    x = []
    for i in range(len(arr)):
        if flag[i] == True:
            # True라면 x에 arr[i]를 arr[i]*2번 추가
            for j in range(2*arr[i]):
                x.append(arr[i])
        else:
            for j in range(arr[i]):
                x.pop()

    return x