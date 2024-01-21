def solution(myString):
    answer = ''
    for i in myString:
        # ordered Alphabet a is at least, z is at most
        if i < 'l':
            answer += 'l'
        else:
            answer += i
    return answer