def solution(arr):
    i = 0
    stk = []
    while i < len(arr):
        if len(stk) == 0 :
            # stk가 빈배열이라면
            stk.append(arr[i])
            i += 1
        else:
            if stk[-1] == arr[i]:
                # stk의 마지막 값과 arr[i]가 같다면
                stk.pop()
                i += 1
            else:
                stk.append(arr[i])
                i += 1
    if len(stk) == 0:
        return [-1]

    return stk