import sys

input = sys.stdin.readline

N = int(input())

tree = []

for _ in range(N):
    tree.append(list(map(int, input().split())))

def print_tree():
    for t in tree:
        for l in t:
            print(l, end = " ")
        print()


for i in range(1, N):
    for j in range(len(tree[i])):
        if j == 0:
            tree[i][j] = tree[i - 1][0] + tree[i][j]
        elif j == len(tree[i]) - 1:
            tree[i][j] = tree[i-1][-1] + tree[i][j]
        else:
            tree[i][j] = max(tree[i-1][j-1], tree[i-1][j],) + tree[i][j]

print(max(tree[N-1]))
