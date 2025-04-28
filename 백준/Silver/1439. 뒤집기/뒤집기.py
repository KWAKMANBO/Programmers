import sys

s = input()

zero_group_cnt = 0
one_group_cnt = 0
cur = True

if s[0] == '1':
    one_group_cnt += 1
    cur = True
else:
    zero_group_cnt += 1
    cur = False

for i in s:
    if cur and i == '0':
        zero_group_cnt += 1
        cur = False
    elif not cur and i == '1':
        one_group_cnt += 1
        cur = True

print(zero_group_cnt if zero_group_cnt < one_group_cnt else one_group_cnt)
