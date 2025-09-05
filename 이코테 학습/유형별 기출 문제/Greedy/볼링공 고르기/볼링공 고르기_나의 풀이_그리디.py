# Input1
# 5 3
# 1 3 2 3 2

# Input2
# 8 5
# 1 5 4 3 2 4 5 2

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

lst = list(map(int, input().split()))

cnts = [lst.count(i) if i in lst else 0 for i in range(m + 1)]

# rest는 아직 처리 되지 않은 볼의 개수
# rest를 왜 사용할까? -> 중복을 발생하지 않도록 잔여개수하고만 계싼하면됨
rest = n
answer = 0

for i in range(1,m+1):
    if cnts[i] != 0:
        rest -= cnts[i]
        answer += cnts[i]*rest
print(answer)
