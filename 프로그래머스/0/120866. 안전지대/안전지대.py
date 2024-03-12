def solution(board):
    answer = 0
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [0,1,-1,1,-1,-1,0,1]
    
    arr = []
    length = len(board)
    for i in range(length):
        for j in range(length):
            if board[i][j] == 1:
                #폭탄이라면
                arr.append([i,j])
    
    for x,y in arr:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < length and 0 <= ny and ny < length:
                # 경계 값을 정해줌
                board[nx][ny] = 1
    
    for i in board:
        answer += i.count(0)
    
    return answer