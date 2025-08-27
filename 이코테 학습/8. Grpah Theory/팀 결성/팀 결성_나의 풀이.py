# Input
# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1

import sys

input = sys.stdin.readline

# n+1은 팀의 개수, m은 연산
n, m = map(int, input().split())
team = [i for i in range(n + 1)]


def find_team(team, x):
    if team[x] != x:
        team[x] = find_team(team, team[x])
    return team[x]


def union_team(team, a, b):
    ta = find_team(team, a)
    tb = find_team(team, b)

    if ta == tb:
        return

    if ta < tb:
        team[tb] = ta
    else:
        team[ta] = tb


for _ in range(m):
    instruction, a, b = map(int, input().split())

    if instruction == 0:
        union_team(team, a, b)
    elif instruction == 1:
        if find_team(team, a) == find_team(team, b):
            print("YES")
        else:
            print("NO")
