def base(num, radix):
    lst = []
    digits = '0123456789ABCDEF'
    if num == 0:
        return '0'

    while num >= radix:
        lst.append(str(digits[num % radix]))
        num //= radix
    lst.append(str(digits[num]))

    return "".join(lst[::-1])


def solution(n, t, m, p):
    answer = ''
    nums = ''
    i = 0
    while len(nums) <= m * t:
        nums += base(i, n)
        i += 1
    for i in range(t):
        answer += nums[(p - 1) + m * i]

    return answer