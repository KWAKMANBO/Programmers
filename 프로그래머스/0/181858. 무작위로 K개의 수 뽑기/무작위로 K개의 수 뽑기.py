def solution(arr, k):
    answer = []
    for i in range(len(arr)):
        if len(answer) <= k-1:
            if arr[i] not in answer:
                answer.append(arr[i])

    if len(answer) < k :
        diff = k - len(answer)
        for i in range(diff):
            answer.append(-1)
    return answer