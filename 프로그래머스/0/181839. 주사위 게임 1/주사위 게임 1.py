def solution(a, b):
    if a % 2 == 1 and b % 2 == 1 :
        # both of them is odd
        return a**2 + b**2
    elif (a % 2 == 1 and b % 2== 0) or (a % 2 == 0 and b % 2 == 1):
        # one of them is odd
        return 2 * (a + b)
    elif a % 2 == 0 and b % 2 == 0:
        return abs(a-b)
