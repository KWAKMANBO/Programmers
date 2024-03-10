def solution(my_string):
    answer = 0
    tmp = ''
    for i in my_string:
        if i.isdigit():
            tmp += i
        else:
            tmp += ' '
    arr = tmp.split()
    for i in arr:
        answer += int(i)
    return answer