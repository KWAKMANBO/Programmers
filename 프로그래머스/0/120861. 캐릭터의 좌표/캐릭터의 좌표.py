def solution(keyinput, board):
    answer = [0,0]
    left = -1*(board[0]//2)
    right = (board[0]//2)
    up = (board[1]//2)
    down = -1*(board[1]//2)
    for i in keyinput:
        if i == "left":
            if answer[0] > left:
                answer[0] -= 1
        elif i == "right":
            if answer[0] < right:
                answer[0] +=1
        elif i == "up":
            if answer[1] < up:
                answer[1] +=1
        elif i == "down":
            if answer[1] > down:
                answer[1] -= 1
    return answer