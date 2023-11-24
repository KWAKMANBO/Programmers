def solution(a, b):
    answer = max(int(str(a) + str(b)), 2 * int(str(a))*int(str(b)))
    return answer