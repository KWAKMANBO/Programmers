import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

first = data[N -1]
second = data[N-2]

# 가장 큰수 더해지는 횟수
count = (M//(K+1))*K
count += M%(K+1)

result = 0
result += count *first
result += (M- count)*second


print(result)