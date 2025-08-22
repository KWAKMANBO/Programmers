# Input
# 6 4
# 1 4
# 2 3
# 2 4
# 5 6

import sys

input = sys.stdin.readline

# 노드와 간선개수 입력
n, m = map(int, input().split())

arr = [i for i in range(n + 1)]


# 부모를 찾는 함수
def find(x):
    # 부모가 0 => 최상위 노드
    if arr[x] == x:
        return x
    else:
        return find(arr[x])


def union(x, y):
    parent_x = find(x)
    parent_y = find(y)

    # y의 부모가 더 작더라면 y를 부모로 만들기
    if parent_y < parent_x:
        arr[parent_x] = parent_y
    else:
        arr[parent_y] = parent_x


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
