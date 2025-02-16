def solution(n):
    if n == 1 : 
        return 1
    elif n == 2 :
        return 2
    n1 = 1
    n2 = 2
    for i in range(n - 2):
        n1, n2 = n2, n1 + n2
    return n2 % 1234567
