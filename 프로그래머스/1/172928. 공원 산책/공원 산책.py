def solution(park, routes):
    height = len(park)
    width = len(park[0])
    x, y = 0, 0

    direction = {
        'S': [1, 0],
        'N': [-1, 0],
        'W': [0, -1],
        'E': [0, 1]
    }

    for i in range(height):
        for j in range(width):
            if park[i][j] == 'S':
                x, y = i, j

    for r in routes:
        dire, dis = r.split()
        dis = int(dis)
        nx, ny = direction[dire]
        move_flag = True
        xx = x
        yy = y

        for _ in range(dis):
            xx += nx
            yy += ny

            if xx > height - 1 or xx < 0 or yy > width - 1 or yy < 0 or park[xx][yy] == 'X':
                move_flag = False
                break

        if move_flag:
            x += nx * dis
            y += ny * dis

    return [x, y]
