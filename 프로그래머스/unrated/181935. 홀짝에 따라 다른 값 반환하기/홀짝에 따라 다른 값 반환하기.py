def solution(n):
    answer = 0
    if n % 2 == 1 :
        for i in range(n + 1):
            answer += isOdd(i)
    else :
        for i in range(n + 1):
            answer += isEven(i)*isEven(i)
    return answer

def isOdd(n):
    if n % 2 == 1 :
        return n
    else:
        return 0
    
def isEven(n):
    if n % 2 == 0:
        return n
    else:
        return 0