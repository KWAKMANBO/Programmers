import sys

string = sys.stdin.readline().rstrip()
answer = 0

for s in string:
    tmp = ord(s)
    if ord('A') <= tmp <= ord('C'):
        answer += 3
    elif ord('D') <= tmp <= ord('F'):
        answer += 4
    elif ord('G') <= tmp <= ord('I'):
        answer += 5
    elif ord('J') <= tmp <= ord('L'):
        answer += 6
    elif ord('M') <= tmp <= ord('O'):
        answer += 7
    elif ord('P') <= tmp <= ord('S'):
        answer += 8
    elif ord('T') <= tmp <= ord('V'):
        answer += 9
    elif ord('W') <= tmp <= ord('Z'):
        answer += 10

print(answer)
