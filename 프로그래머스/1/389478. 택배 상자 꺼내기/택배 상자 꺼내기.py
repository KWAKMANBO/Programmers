def solution(n, w, num):
    answer = 0
    # 각 board에는 같은 행에 속하는 숫자들이 속하게하기 위해 w만큼 리스트 추가
    board = [[] for _ in range(w)]
    direction = True
    for i in range(n):
        if i % w == 0 and i != 1 and i != 0:
            direction = not direction
        if direction:
            board[i%w].append(i+1)
        else:
            board[w - 1 - i%w].append(i+1)


    for b in board:
        if num in b:
            idx = b.index(num)
            answer = len(b[idx:])

    return answer