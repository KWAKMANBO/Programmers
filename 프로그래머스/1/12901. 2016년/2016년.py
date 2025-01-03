day = {0: 'THU', 1: 'FRI', 2: 'SAT', 3: 'SUN', 4: 'MON', 5: 'TUE', 6: 'WED'}
month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def solution(a, b):
    n = 0
    for i in range(a - 1):
        n += month[i]
    n += b
    return day[(n % 7)]