def solution(triangle):
    dp = [[0] * len(t) for t in triangle]

    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            elif 0 < j < len(triangle[i]) - 1:
                dp[i][j] = max(dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j])
            elif j == len(triangle[i]) - 1:
                dp[i][j] = dp[i-1][j-1] +  triangle[i][j]

    return max(dp[len(triangle)-1])
