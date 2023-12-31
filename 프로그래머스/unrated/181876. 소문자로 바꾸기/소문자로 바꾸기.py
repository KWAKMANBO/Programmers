def solution(myString):
    answer = ''
    for i in range(len(myString)):
        if myString[i].isupper():
            answer += myString[i].lower()
        else:
            answer += myString[i]
    return answer