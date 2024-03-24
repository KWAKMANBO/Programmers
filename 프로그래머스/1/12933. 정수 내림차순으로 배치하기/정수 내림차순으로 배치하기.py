def solution(n):
    num = str(n)
    string = ''
    tmp = [i for i in num]
    tmp.sort()
    tmp.reverse()
    for i in tmp:
        string += i
          
    return int(string)