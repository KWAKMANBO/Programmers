def solution(X, Y):
    answer = ''
    # 9부터 0까지 for문을 돌려야 정렬할 필요가 없어 효율적임
    for i in range(9, -1, -1):
        num = str(i)
        answer += num * min(X.count(num), Y.count(num))
    if not answer:
        answer = "-1"
    elif len(answer) == answer.count('0'):
        answer = "0"
        
    return answer