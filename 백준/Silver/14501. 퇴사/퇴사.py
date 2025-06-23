import sys  
  
input = sys.stdin.readline  
  
N = int(input())  
works = [list(map(int, input().split())) for _ in range(N)]  
  
dp = [0] * (N + 1)  
  
for i in range(N):  
    for j in range(i + works[i][0], N + 1):  
        # dp에는 최정적으로 각날짜의 최댓값이 저장되게됨  
        if dp[j] < dp[i] + works[i][1]:  
            # j는 i번쨰 일이 끝난 이후를 의미  
            dp[j] = dp[i] + works[i][1]  
  
print(dp[-1])
