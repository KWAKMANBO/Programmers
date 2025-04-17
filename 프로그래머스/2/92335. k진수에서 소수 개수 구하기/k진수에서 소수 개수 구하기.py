def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def to_base(n, k):
    if k == 10:
        return str(n)
    tmp = ''
    while n > 0:
        tmp += str(n % k)
        n //= k
    return tmp[::-1]


def solution(n, k):
    answer = 0
    lst = []
    base = to_base(n, k)
    nums = []
    for b in base.split('0'):
        if b:
            nums.append(int(b))
    for n in nums:
        if n and is_prime(n):
            answer += 1
    return answer