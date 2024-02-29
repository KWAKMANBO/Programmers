def solution(balls, share):
    answer = 0
    return (fact(balls)//(fact(balls-share)*(fact(share))))

def fact(n):
    num = 1
    for i in range(1,n+1):
        num *= i
    print(num)
    return num