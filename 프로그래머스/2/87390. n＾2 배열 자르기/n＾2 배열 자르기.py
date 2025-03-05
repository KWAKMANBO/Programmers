def solution(n, left, right):
    answer = []

    while left <= right:
        r = left // n
        c = left % n
        if r > c:
            answer.append(r + 1)
        else:
            answer.append(c + 1)
        left += 1

    return answer