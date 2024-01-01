def solution(arr, query):
    answer = arr
    for i in range(len(query)):
        if i % 2 == 0:
            #짝수 일때
            answer = answer[0:query[i]+1]
        else:
            #홀수 일때
            answer = answer[query[i]:]
        
    return answer