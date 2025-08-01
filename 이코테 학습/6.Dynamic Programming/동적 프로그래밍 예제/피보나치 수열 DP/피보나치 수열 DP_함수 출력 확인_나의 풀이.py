dp = [0] * 101


def fibo_print(x):
    print(f"fibo({x})", end="->")
    if x == 1 or x == 2:
        return 1

    if dp[x] != 0:
        return dp[x]

    dp[x] = fibo_print(x - 1) + fibo_print(x - 2)
    return dp[x]


fibo_print(6)
