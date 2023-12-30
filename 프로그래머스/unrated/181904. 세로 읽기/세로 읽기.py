def solution(my_string, m, c):
    answer = ''
    r = len(my_string)//m
    arr = [['' for _ in range(m)] for _ in range(r)]
    #m은 열 r은 행
    idx = 0
    for i in range(r):
        for j in range(m):
            arr[i][j] = my_string[idx]
            idx +=1
    for i in range(r):
        answer += arr[i][c-1]
    return answer