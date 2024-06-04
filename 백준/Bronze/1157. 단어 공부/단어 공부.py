import sys

line = sys.stdin.readline().rstrip()

line = line.upper()

s = set(line)
answer = ''
cnt = 0
for i in s:
    if line.count(i) > cnt:
        answer = i
        cnt = line.count(i)
    elif line.count(i) == cnt:
        answer = "?"

print(answer)
