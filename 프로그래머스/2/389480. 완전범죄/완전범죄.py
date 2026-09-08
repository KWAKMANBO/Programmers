# info 훔칠 리스트
# n은 A의 최대 흔적
# m은 B의 최대 흔적


def solution(info, n, m):
    INF = 1e10

    dp = [INF] * m

    dp[0] = 0

    for a, b in info:
        tmp = [INF] * m
        for i in range(m):

            # dp[i]가 INF면 굳이 비교할 이유 X
            if dp[i] == INF:
                continue

            # i는 b의 상태를 의미
            # dp[i]는 b일때 a의 상태중 최솟값을 저장
            # a가 훔친 경우
            if dp[i] + a < n:
                tmp[i] = min(dp[i] + a, tmp[i])
            # b가 훔친 경우
            if i + b < m:
                tmp[i + b] = min(dp[i], tmp[i + b])

        dp = tmp

    answer = min(dp)

    return answer if answer != INF else -1