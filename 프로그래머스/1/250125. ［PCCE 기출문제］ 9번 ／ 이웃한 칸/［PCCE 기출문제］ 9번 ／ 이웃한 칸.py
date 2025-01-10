def solution(board, h, w):
    answer = 0
    value = board[h][w]

    if h - 1 >= 0 and value == board[h - 1][w]:
        answer += 1
    if h + 1 < len(board) and value == board[h + 1][w]:
        answer += 1
    if w - 1 >= 0 and value == board[h][w - 1]:
        answer += 1
    if w + 1 < len(board[0]) and value == board[h][w + 1]:
        answer += 1

    return answer