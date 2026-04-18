from itertools import permutations
from itertools import combinations

def solution(numbers):
    numbers = list(numbers)

    def is_prime(n):
        # print(f"n : {n}")
        if n == 1 or n == 0:
            return 0
        for i in range(2, int(n ** 0.5) + 1 ):
            if n % i == 0:
                return 0
        return str(n)

    answer = set()
    for i in range(1, len(numbers)+1):
        for c in combinations(numbers, i):
            for n in permutations(c):
                tmp = int("".join(n))
                if is_prime(tmp):
                    answer.add(tmp)



    return len(answer)