import sys

n = int(sys.stdin.readline().rstrip())
answer = n

for _ in range(n):
    tmp = sys.stdin.readline().rstrip()
    stmp = set(tmp)

    for i in stmp:
        idx = tmp.index(i)
        cnt = 0
        for j in range(idx, len(tmp)):
            if tmp[j] == i:
                cnt += 1
            else:
                break
        if cnt != tmp.count(i):
            answer -= 1
            break

print(answer)
