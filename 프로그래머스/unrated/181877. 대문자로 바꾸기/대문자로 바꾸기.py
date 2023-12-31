def solution(myString):
    answer = ''
    for i in myString:
        if not i.isupper()  :
            i = i.upper()
        answer += i
    return answer
