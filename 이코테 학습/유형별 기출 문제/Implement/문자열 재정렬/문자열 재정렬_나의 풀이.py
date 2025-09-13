# input1
# K1KA5CB7

# Input2
# AJKDLSI412K4JSJ9D

import sys

input = sys.stdin.readline

s = list(input().strip())

s.sort()

num = 0
answer = ""
for i in s:
    if i.isdigit():
        num += int(i)
    else:
        answer += i
print(answer+str(num))