import sys

degrees = []

for _ in range(3):
    degrees.append(int(sys.stdin.readline().rstrip()))
if sum(degrees) == 180 and len(set(degrees)) == 1:
    print("Equilateral")
elif sum(degrees) == 180 and len(set(degrees)) == 2:
    print("Isosceles")
elif sum(degrees) == 180 and len(set(degrees)) == 3:
    print("Scalene")
else:
    print("Error")