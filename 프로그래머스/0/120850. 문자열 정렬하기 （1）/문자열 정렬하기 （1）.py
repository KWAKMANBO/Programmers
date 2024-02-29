def solution(my_string):
    answer = []
    #'0' -> 48 '9' -> 57
    for i in my_string:
        if ord(i) > 47 and ord(i) < 58:
            answer.append(ord(i) - 48)
        answer.sort()
    return answer