import sys

line = sys.stdin.readline().rstrip().split("-")

answer = 0

if "+" in line[0]:
    tmp = line[0].split("+")
    for i in tmp:
        answer += int(i)
else:
    answer += int(line[0])

for i in line[1:]:
    if "+" in i:
        tmp = i.split("+")
        for j in tmp:
            answer -= int(j)
    else:
        answer -= int(i)

print(answer)
