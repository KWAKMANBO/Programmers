import sys

input = sys.stdin.readline

N = int(input())

if N == 1 or N == 2:
    print(1)

num = 0
cnt = 0
for i in range(3,N+1,2):
    num += i
    cnt +=1
    if num >= N:
        print(cnt)
        break

