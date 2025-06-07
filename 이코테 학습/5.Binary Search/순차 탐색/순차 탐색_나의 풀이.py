# Input1
# 5 Dongbin
# Hanul Jonggu Dongbin Taeil Sangwook

import sys

input = sys.stdin.readline

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")

# 문자열 입력받기
n, target = input().split()

print("앞서 적은 원소의 개수만큼 문자열을 입력해주세요, 구분은 띄어쓰기 한 칸으로 합니다.")
lst = input().split()

for i in range(int(n)):
    if lst[i] == target:
        print(i + 1)
        break
