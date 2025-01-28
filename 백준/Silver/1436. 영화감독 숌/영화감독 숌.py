# 666이 들어가는 수를 순서대로 구하라


n = int(input())


def find(n):
    i = 666
    count = 0
    while True:
        if '666' in str(i):
            count += 1

        if count == n:
            return str(i)

        i += 1


print(find(n))
