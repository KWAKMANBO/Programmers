import sys


def gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


fraction1, denominator1 = map(int, sys.stdin.readline().split())
fraction2, denominator2 = map(int, sys.stdin.readline().split())

common_denominator = lcm(denominator1, denominator2)
common_fraction = fraction1 * (common_denominator // denominator1) + fraction2 * (common_denominator // denominator2)

common_gcd = gcd(common_denominator,common_fraction)


print(f"{common_fraction//common_gcd} {common_denominator//common_gcd}")
