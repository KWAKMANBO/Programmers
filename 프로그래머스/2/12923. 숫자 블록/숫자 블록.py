import math


# 블록의 길이 10^9
# 블록에 적힐 숫자는 1~10^7 까직 가능
def solution(begin, end):
    def find(n):
        if n == 1:
            return 0

        max_div = 1

        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                if n // i <= 1e7:
                    return n // i
                else:
                    max_div = i

        return max_div

    return [find(i) for i in range(begin, end + 1)]