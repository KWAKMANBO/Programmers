from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    return 0


def solution(numbers):
    numbers = list(map(str, numbers))

    numbers.sort(key=cmp_to_key(compare))

    return "".join(numbers) if int("".join(numbers)) != 0 else "0"


