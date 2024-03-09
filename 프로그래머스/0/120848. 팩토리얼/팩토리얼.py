def solution(n):
    answer = 0
    val = fact(1)
    i = 1
    while val < n:
        i+=1
        val = fact(i)
        
    if val == n :
        return i
    else:
        return i-1
        

def fact(n):
    val =1
    for i in range(2,n+1):
        val *= i
    return val