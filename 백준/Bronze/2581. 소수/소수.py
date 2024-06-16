import sys
s = int(sys.stdin.readline().rstrip())
e = int(sys.stdin.readline().rstrip())


answer = []

for i in range(s,e+1):
    tmp = 0
    for j in range(1, (i // 2) + 1):
        if i % j == 0:
            tmp += 1
    tmp += 1
    if tmp == 2:
        answer.append(i)

if len(answer) == 0 :
    print(-1)
else:
    print(sum(answer))
    print(min(answer))
