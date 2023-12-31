def solution(n, k):
    
    answer = []
    m = n//k
    
    return [k*i for i in range(m+1) if i > 0]