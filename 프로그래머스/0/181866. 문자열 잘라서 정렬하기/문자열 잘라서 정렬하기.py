def solution(myString):
    str =  myString.split('x')
    str.sort()
    if '' in str:
        for i in range(str.count('')):
            str.remove('')
    return str