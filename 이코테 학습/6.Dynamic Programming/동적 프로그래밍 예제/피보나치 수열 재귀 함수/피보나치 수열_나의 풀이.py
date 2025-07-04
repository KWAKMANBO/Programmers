# 재귀 함수 방식으로 피보나치 수열을 구현하게되면
# n이 커질 수록 시간이 오래걸리는 문제가 발생
# 예를 들어 N이 30이면 약 10억 가량의 연산을 수행해야함
def fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(4))
