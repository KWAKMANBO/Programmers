# Input
# 4 6
# 19 15 10 17
# 나의 풀이를 개선한 버전으로 답을 참고해서 나만의 코드로 작성했다


import sys

input = sys.stdin.readline

N, M = map(int, input().split())

rices = list(map(int, input().split()))
start = 0
end = max(rices)


def get_sum(arr, height):
    lst = [i - height for i in arr if i > height]
    return sum(lst)


answer = []
while start <= end:
    height = (start + end) // 2

    if get_sum(rices, height) >= M:
        # 떡의 길이의 합을 줄여야함 -> height의 크기를 높여야함-> start를 올리기
        answer.append(height)
        start = height + 1
    elif get_sum(rices, height) < M:
        # 떡의 길이의 합을 늘려야함 -> height의 크기를 줄이기 -> end를 내리기
        end = height - 1
    else:
        answer.append(height)
        break

print(max(answer))
