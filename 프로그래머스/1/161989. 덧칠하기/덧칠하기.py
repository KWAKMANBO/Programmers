def solution(n, m, section):
    answer = 1
    start = 0
    end = 1
    while end < len(section):
        if section[end] - section[start] >= m:
            answer += 1
            start = end
        end += 1

    return answer
