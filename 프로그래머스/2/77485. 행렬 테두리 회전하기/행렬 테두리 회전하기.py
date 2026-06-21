def solution(rows, columns, queries):
    answer = []
    # 초기화
    board = [[r * columns + c + 1 for c in range(columns)] for r in range(rows)]

    for q in queries:

        si, sj, ei, ej = q[0] - 1, q[1] - 1, q[2] - 1, q[3] - 1
        min_num = board[si][sj]
        move_lst = [(si, ej), (ei, ej), (ei, sj), (si, sj)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        previous = board[si][sj]
        for i in range(4):
            sr, sc = move_lst[i - 1]
            er, ec = move_lst[i]
            dir = directions[i]


            while True:
                nr = sr + dir[0]
                nc = sc + dir[1]


                tmp = board[nr][nc]
                min_num = min(min_num,tmp)
                board[nr][nc] = previous
                previous = tmp
                sr,sc = nr,nc

                if (sr,sc) == (er,ec):
                    break
        answer.append(min_num)


    return answer