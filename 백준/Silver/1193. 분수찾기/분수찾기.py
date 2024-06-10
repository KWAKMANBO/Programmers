import sys

n = int(sys.stdin.readline().rstrip())
line = 1
tmp = n
while n > line:
    n -= line
    line += 1

for i in range(1, line):
    tmp -= i

if line % 2 == 0:
    print(f"{tmp}/{(line + 1) - tmp}")
else:
    print(f"{(line + 1) - tmp}/{tmp}")
