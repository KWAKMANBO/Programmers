import sys

n = int(sys.stdin.readline().rstrip())

numbers = [i for i in sys.stdin.readline().rstrip().split()]

num = sys.stdin.readline().rstrip()

print(numbers.count(num))
