a, b = map(int, input().split())

ai = list(map(int, input().split()))
bi = list(map(int, input().split()))

answer = sum(ai)

for i in bi:
    if i != 0 :
        answer *= i
print(answer)
