import sys

n = int(sys.stdin.readline().rstrip())

numbers = [int(i) for i in sys.stdin.readline().rstrip().split()]

print(min(numbers), max(numbers))
