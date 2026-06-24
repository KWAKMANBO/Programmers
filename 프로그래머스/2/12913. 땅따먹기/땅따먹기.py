def solution(land):
    dp = land

    for i in range(1, len(dp)):
        for j in range(len(dp[0])):
            tmp = []
            for k in range(len(dp[0])):
                if k != j:
                    tmp.append(dp[i-1][k])

            dp[i][j] = max(tmp) + land[i][j]



    return max(dp[-1])