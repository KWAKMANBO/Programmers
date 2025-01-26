import sys

w, h = map(int, sys.stdin.readline().split())

board = []

answer = []


def check(board, sr, sc):
    wb = "WBWBWBWB"
    bw = "BWBWBWBW"
    cnt1 = 0
    cnt2 = 0
    for r in range(sr, sr + 8):
        for c in range(sc, sc + 8):
            if r % 2 == 0:
                if board[r][c] != wb[c-sc]:
                    cnt1 += 1
                if board[r][c] != bw[c-sc]:
                    cnt2 += 1
            else:
                if board[r][c] != bw[c-sc]:
                    cnt1 += 1
                if board[r][c] != wb[c-sc]:
                    cnt2 += 1
    return min(cnt1, cnt2)


for _ in range(w):
    board.append(sys.stdin.readline().strip())

for i in range(w - 8 + 1):
    for j in range(h - 8 + 1):
        answer.append(check(board, i, j))

print(min(answer))
