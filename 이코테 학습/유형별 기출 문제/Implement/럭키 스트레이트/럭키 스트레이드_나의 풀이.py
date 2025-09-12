import sys

input = sys.stdin.readline

number = input().strip()
length = len(number)


def sum_each_num(num):
    sum_num = 0
    for n in num:
        sum_num += int(n)
    return sum_num


left = number[:length // 2]
right = number[length // 2 :]

if sum_each_num(left) == sum_each_num(right):
    print("LUCKY")
else:
    print("READY")