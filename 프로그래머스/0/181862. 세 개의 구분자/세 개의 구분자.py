def solution(myStr):
    str = myStr
    str = str.replace('a', '1')
    str = str.replace('b', '1')
    str = str.replace('c', '1')
    answer = str.split('1')

    for i in range(answer.count('')):
         answer.remove('')

    if answer == []:
        answer.append('EMPTY')
        return answer

    return answer