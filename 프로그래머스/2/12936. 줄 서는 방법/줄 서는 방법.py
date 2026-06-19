from collections import deque


def solution(n, k):
    answer = []
    k -= 1
    lst = [i for i in range(1, n + 1)]

    fact = deque()
    tmp = 1
    for i in range(1, n):
        tmp *= i
        fact.append(tmp)
    fact.reverse()
    fact += [1]

    for _ in range(n):
        f = fact.popleft()
        answer.append(lst.pop(k//f))
        k %= f


    return answer