def solution(n):
    arr = []
    for i in range(1,n//2+1):
        if n % i == 0:
            arr.append(i)
    arr.append(n)
    return sum(arr)