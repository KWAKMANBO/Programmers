def solution(n):
    even = [i for i in range(2,n+1,2)]
    sum = 0
    for i in even:
        sum += i
    return sum