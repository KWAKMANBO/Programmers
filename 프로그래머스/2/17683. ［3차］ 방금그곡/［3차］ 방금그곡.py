def solution(m, musicinfos):
    answer = []
    for i in "C#", "D#", "F#", "G#", "A#":
        m = m.replace(i, i[0].lower())
    order = 0
    for music in musicinfos:
        st, et, title, lyric = music.split(',')
        st = int(st[:2]) * 60 + int(st[3:])
        et = int(et[:2]) * 60 + int(et[3:])
        for i in "C#", "D#", "F#", "G#", "A#":
            lyric = lyric.replace(i, i[0].lower())

        play_time = et - st
        play = lyric * (play_time // len(lyric)) + lyric[:play_time % len(lyric)]

        if m in play:
            answer.append([title, play_time, order])
            order += 1
    answer.sort(key=lambda x: (-x[1], x[2]))
    return answer[0][0] if answer else "(None)"