# Input1
# 5 3
# 1 3 2 3 2

# Input2
# 8 5
# 1 5 4 3 2 4 5 2

n,m = map(int, input().split())

data = list(map(int, input().split()))

array = [0]*11

for x in data:
    array[x] +=1
result = 0
for i in range(1, m+1):
    n -= array[i]
    result += array[i]*n

print(result)