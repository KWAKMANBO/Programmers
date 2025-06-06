import sys

input = sys.stdin.readline

N = int(input())
books = [input().strip() for _ in range(N)]

visited = []
lst = []
for b in books:
    if b not in visited:
        visited.append(b)
        books.append(b)
        lst.append([b, books.count(b)])
lst.sort(key=lambda x: (-x[1], x[0]))
print(lst[0][0])
