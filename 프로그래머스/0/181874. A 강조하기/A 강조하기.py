def solution(myString):
    answer = ''
    for i in myString:
        if i == 'a':
            answer += 'A'
        elif i == 'A':
            answer += i
        else:
            if i.isupper():
                answer += i.lower()
            else:
                answer += i
    return answer