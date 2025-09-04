import sys

input = sys.stdin.readline

bins = input().strip()
zero = 0
one = 0
cur = True

if bins[0] == '0':
    zero += 1
    cur = False
else:
    one += 1
    cur = True

for b in bins:
    # 현재 zero 그룹인데 1로 바뀐다면
    if b == '1' and not cur:
        one += 1
        cur = True
    elif b == "0" and cur:
        zero += 1
        cur = False

answer = min(zero, one)
print(answer)
