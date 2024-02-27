def solution(slice, n):
    for i in range(n+1):
        if i*slice >= n:
            return i