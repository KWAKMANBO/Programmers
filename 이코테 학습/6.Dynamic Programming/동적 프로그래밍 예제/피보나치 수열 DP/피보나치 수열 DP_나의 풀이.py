dp = [0] * 100

def fibo_recursive(n):
    if n == 1 or n == 2:
        return 1
    if dp[n]:
        return dp[n]

    dp[n] = fibo_recursive(n - 1) + fibo_recursive(n - 2)

    return dp[n]
fibo_recursive(99)
print(dp[99])

