def solution(m, n, board):
    answer = 0
    board = [list(b) for b in board]

    def view(board):
        for b in board:
            for i in b:
                print(i, end=" ")
            print()

    def check(si, sj):
        tmp = set()
        for di, dj in ((0, 0), (1, 0), (0, 1), (1, 1)):
            ni, nj = si + di, sj + dj
            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == board[si][sj]:
                tmp.add((ni, nj))
            else:
                return set()
        else:
            return tmp

    def move(board):
        new_board = [[i for i in b] for b in board]
        for j in range(n):
            for i in range(m - 1, 0, -1):
                if new_board[i][j] == 0:
                    for ii in range(i, -1, -1):
                        if new_board[ii][j] != 0:
                            new_board[i][j] = new_board[ii][j]
                            new_board[ii][j] = 0
                            break
        return new_board

    flag = False
    while not flag:

        lst = set()

        for i in range(m):
            for j in range(n):
                tmp = check(i, j)
                lst = lst.union(tmp)

        for l in lst:
            board[l[0]][l[1]] = 0

        new_board = move(board)
        if board == new_board:
            flag = True
        else:
            board = new_board

    for i in board:
        for j in i:
            if j == 0:
                answer += 1

    return answer