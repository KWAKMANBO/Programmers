def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    m, s = map(int, video_len.split(":"))
    video_len_sec = m * 60 + s

    m, s = map(int, pos.split(":"))
    pos_sec = m * 60 + s

    m, s = map(int, op_start.split(":"))
    op_start_sec = m * 60 + s

    m, s = map(int, op_end.split(":"))
    op_end_sec = m * 60 + s

    for c in commands:
        if op_start_sec <= pos_sec < op_end_sec:
            pos_sec = op_end_sec

        if c == "prev":
            pos_sec -= 10
            if pos_sec < 0:
                pos_sec = 0
        if c == "next":
            pos_sec += 10

        if op_start_sec <= pos_sec < op_end_sec:
            pos_sec = op_end_sec

        if pos_sec > video_len_sec:
            pos_sec = video_len_sec
    MM = pos_sec // 60
    SS = pos_sec % 60
    return f"{MM:02d}:{SS:02d}"