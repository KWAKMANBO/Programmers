import sys

input = sys.stdin.readline

N = int(input())

lst = sorted(list(map(int, input().split())))

start = 0
end = N - 1

answer = abs(lst[start] + lst[end])
answer_idx = [lst[start], lst[end]]

while start < end:
    l, r = lst[start], lst[end]
    s = l + r
    absol_s = abs(s)

    if absol_s < answer:
        answer = absol_s
        answer_idx = [l, r]


    if s < 0:
        # 음수라면 크기를 키워야함
        start += 1
    else:
        # 양수라면 크기를 줄여야함
        end -= 1

print(answer_idx[0], answer_idx[1])
