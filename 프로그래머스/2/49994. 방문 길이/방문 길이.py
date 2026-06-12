def solution(dirs):
    direction = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

    cur_pos = (0, 0)

    visited = set()
    for d in dirs:
        cx, cy = cur_pos
        dx, dy = direction[d]
        nx, ny = cx + dx, cy + dy
        # print(f"cur : {(cx, cy)}, next : {(nx, ny)}")
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            cur_pos = (nx, ny)
            if cx > nx:
                nx, cx = cx, nx
            if cy > ny:
                cy, ny = ny, cy
            visited.add((cx, cy, nx, ny))

    return len(visited)