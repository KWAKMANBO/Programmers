def solution(a, b):
    answer = 0
    num = gcd(a,b)
    if num != 1:
        # gcd가 1이 아니라면
        a = a// num
        b = b// num
    
    arr = []
    while b != 1:
        if b % 5 == 0:
            b = b//5
            arr.append(5)
        elif b % 2 == 0:
            b = b//2
            arr.append(2)
        else:
            arr.append(b)
            b = b//b
    if len(arr) == arr.count(2) + arr.count(5):
        return 1
    else:
        return 2

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    