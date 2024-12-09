def gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        r = a % b
        a, b = b, r
    return a

def lcd(a, b):
    return a * b // gcd(a, b)


def solution(n, m):
    return [gcd(n,m), lcd(n,m)]