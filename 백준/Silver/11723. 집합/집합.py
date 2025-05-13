import sys

input = sys.stdin.readline

N = int(input())
s = set()

for _ in range(N):
    inp = input().split()
    instruction, num = '', ''

    if len(inp) == 2:
        instruction, num = inp[0], int(inp[1])
    else:
        instruction = inp[0]

    if instruction == 'add':
        s.add(num)
    elif instruction == 'remove':
        if num in s:
            s.remove(num)
    elif instruction == 'check':
        if num in s:
            print('1')
        else:
            print('0')
    elif instruction == 'toggle':
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    elif instruction == 'all':
        s = set(i for i in range(1, 21))
    elif instruction == 'empty':
        s = set()
