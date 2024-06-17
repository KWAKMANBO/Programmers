import sys

# 삼각형의 조건
# 두변이 길이의 합이 가장 큰 변과 같거나 작으면 삼각형이 될 수 없음

while True:
    lines = list(map(int, sys.stdin.readline().rstrip().split()))
    lines.sort()

    if lines.count(0) == 3:
        break
    else:
        if lines[2] >= lines[0] + lines[1]:
            print("Invalid")
        else:
            if len(set(lines)) == 1:
                print("Equilateral")
            elif len(set(lines)) == 2:
                print("Isosceles")
            elif len(set(lines)) == 3:
                print("Scalene")
