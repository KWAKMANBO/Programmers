def solution(numer1, denom1, numer2, denom2):
    numer = numer1*denom2 + numer2*denom1
    denom = denom1*denom2
    tmp = gcd(numer,denom)
    answer = [numer//tmp, denom//tmp]
    return answer

def gcd(m,n):
    if m < n :
        m , n = n, m
    
    if m % n == 0 : 
        return n
    else:
        return gcd(n, m%n)