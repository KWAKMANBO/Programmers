import sys

input = sys.stdin.readline

N = input()
answer = 0
for i in range(int(N) + 1):
    for j in range(60):
        for k in range(60):
            # 3중 for문을 이용해서 숫자를 카운팅
            time = str(i) + str(j) + str(k)
            # 3이 있는지 확인하기 위해서 i,j,k를 문자열로 변경
            if '3' in time:
                answer += 1

print(answer)
# 답안 코드와 내 풀이의 로직이 동일해 답안 코드 작성은 SKIP