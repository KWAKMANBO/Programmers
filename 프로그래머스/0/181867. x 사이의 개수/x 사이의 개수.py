def solution(myString):
    tmp = myString.split('x')
    answer = []
    for i in tmp:
        answer.append(len(i))
    return answer