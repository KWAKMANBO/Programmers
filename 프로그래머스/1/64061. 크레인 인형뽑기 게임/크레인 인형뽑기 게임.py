def solution(board, moves):
    answer = 0
    basket = []
    for m in moves:
        for i in range(len(board)):
            if board[i][m - 1] != 0:
                basket.append(board[i][m - 1])
                board[i][m - 1] = 0
                break
        while len(basket) > 1 and basket[-1] == basket[-2]:
            answer += 2
            for _ in range(2):
                basket.pop()

    return answer