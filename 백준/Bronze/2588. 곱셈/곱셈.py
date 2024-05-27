import sys

a= sys.stdin.readline()
b = sys.stdin.readline()

a = int(a)
b = [int(b[0]), int(b[1]), int(b[2]), int(b)]

print(a*b[2])
print(a*b[1])
print(a*b[0])
print(a*b[3])
