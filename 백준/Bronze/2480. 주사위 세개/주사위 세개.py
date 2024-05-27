import sys

dice = list((map(int, sys.stdin.readline().split())))
set_dice = set(dice)

if len(set_dice) == 1:
    print(10000 + dice[0] * 1000)
elif len(set_dice) == 2:
    for i in set_dice:
        if dice.count(i) == 2:
            print(1000 + i * 100)
else:
    print(max(dice) * 100)
