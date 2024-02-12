def solution(n):
    if n == 1:
        return [[1]]
    
    answer = [[0 for i in range(n)] for j in range(n)]
    
    col = 0
    row = 0
    direction = 'r'
    
    for i in range(n*n):
        answer[row][col] = i+1
        if direction == 'r':
            col += 1
            if col == n - 1 or answer[row][col+1] != 0:
                direction = 'd'
        elif direction == 'd':
            row += 1
            if row == n -1 or answer[row+1][col] != 0 :
                direction = 'l'
        elif direction == 'l':
            col -= 1
            if col == 0 or answer[row][col-1] != 0:
                direction = 'u'
        else:
            row -= 1
            if row == 0 or answer[row-1][col] != 0 :
                direction = 'r'
            
            
    
    return answer