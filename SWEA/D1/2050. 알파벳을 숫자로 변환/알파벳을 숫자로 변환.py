
line = input()

result = []

for i in line:
    result.append(ord(i)-64)

print(" ".join(map(str,result)))