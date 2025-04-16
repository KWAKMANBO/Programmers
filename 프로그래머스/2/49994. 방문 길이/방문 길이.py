def solution(dirs):
    answer = 0
    pos = (0, 0)
    move_lst = set()
    dir_dict = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    for d in dirs:
        dx, dy = dir_dict[d]
        x, y = pos
        nx, ny = x + dx, y + dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            pos = (nx, ny)
            move_lst.add((x, y, nx, ny))
            move_lst.add((nx, ny, x, y))

    return len(move_lst)//2