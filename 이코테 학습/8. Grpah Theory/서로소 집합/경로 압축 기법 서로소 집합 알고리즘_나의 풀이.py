# Input
# 6 4
# 1 4
# 2 3
# 2 4
# 5 6

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [i for i in range(n + 1)]


# 부모로 최상위 노드를 지정
def find(x):
    if arr[x] == x:
        return arr[x]
    else:
        return find(arr[x])


def union(x, y):
    parent_x = find(x)
    parent_y = find(y)

    if parent_x < parent_y:
        arr[parent_y] = parent_x
    else:
        arr[parent_x] = parent_y


for _ in range(m):
    s, e = map(int, input().split())
    union(s, e)

# 원소가 속한 집합의 부모를 출력하기
roots = [find(i) for i in range(1, n + 1)]
print(f"각 원소가 속한 집합 :", end=" ")
for r in roots:
    print(r, end=" ")
print()
# 각 원소의 부모 출력
print(f"부모 테이블 : ", end=" ")
for a in arr[1:]:
    print(a, end=" ")
