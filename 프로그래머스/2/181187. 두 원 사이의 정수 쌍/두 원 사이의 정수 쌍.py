import math

def solution(r1, r2):
    answer = 0

    def calculate(r):
        k = 0
        for i in range(r + 1):
            y_sq = r ** 2 - i ** 2
            k += math.isqrt(y_sq) + 1

        return 4 * k - 4 * r - 3

    def border(r):
        k = 0
        for i in range(1,r):
            y_sq = r ** 2 - i ** 2
            y_int = math.isqrt(y_sq)
            if y_sq == y_int*y_int:
                k += 1

        return 4*k + 4

    point1 = calculate(r1)
    point2 = calculate(r2)
    bor = border(r1)


    return point2 - point1 + bor