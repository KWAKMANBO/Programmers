import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    a = denom1 * denom2
    b = denom1*numer2 + denom2*numer1
    c = math.gcd(a,b)
    answer.append(b//c)
    answer.append(a//c)
    return answer
    
