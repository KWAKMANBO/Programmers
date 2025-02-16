def gcd(x, y):
    if x < y:
        x, y = y, x

    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


def solution(arr):
    answer = arr[0]
    for i in arr[1:]:
        answer = lcm(answer,i)
    return answer