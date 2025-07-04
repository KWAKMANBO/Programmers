# 재귀 함수 방식으로 피보나치 수열을 구현하게되면
# n이 커질 수록 시간이 오래걸리는 문제가 발생
# 예를 들어 N이 30이면 약 10억 가량의 연산을 수행해야함
def fibo(x):
    if x == 1 or x == 2:
        return 1

    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))
