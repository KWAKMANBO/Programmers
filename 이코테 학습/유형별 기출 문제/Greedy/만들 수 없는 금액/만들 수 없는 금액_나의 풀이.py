# 5
# 3 2 1 1 9

# 풀이 방법
# target은 현재 만들 수 있는 돈의 크기를 의미 target = n이면 n-1까진 만들 수 있음
# 1. target = 1 로 설정
# 2. coin 배열 오름차순으로 정렬
# 3. coin에서 하나싞 target이랑 비교하기
#   4-1. 현재 동전이 target 보다 크면 break
#   4-2. 현재 동전이 target 보다 작으면 target + 현재 동전해서 target을 업데이트

import sys

input = sys.stdin.readline

n = int(input())

coin = list(map(int, input().split()))
coin.sort()

target = 1

for c in coin:
    if target < c:
        break
    else:
        target += c

print(target)
