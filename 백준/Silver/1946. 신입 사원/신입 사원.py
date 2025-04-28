import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(list(map(int, input().split())))
    lst.sort()
    # 첫번째 원소는 낮은순으로 정렬
    # 두번재 원소는
    second = -1
    answer = 1
    rank = lst[0][1]
    for i in range(1, n):
        if rank > lst[i][1]:
            answer += 1
            rank = lst[i][1]

    print(answer)
