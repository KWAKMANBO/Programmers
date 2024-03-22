def solution(n):
    answer = 0
    num_str = str(n)
    print(num_str)
    for i in num_str:
        answer += int(i)

    return answer