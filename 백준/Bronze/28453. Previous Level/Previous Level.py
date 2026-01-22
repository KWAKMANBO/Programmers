n = int(input())

levels = list(map(int, input().split()))

answer = []

for l in levels:
    if l < 250:
        answer.append("4")
    elif 250 <= l < 275:
        answer.append("3")
    elif 275 <= l < 300:
        answer.append("2")
    else:
        answer.append("1")

print(" ".join(answer))
