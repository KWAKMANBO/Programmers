def solution(wallpaper):
    answer = []
    s = [100, 100]
    e = [100, -1]
    # 시작점 찾기(행)
    for i in range(len(wallpaper)):
        if "#" in wallpaper[i]:
            s[0] = i
            break
    # 시작점 찾기(열)
    for i in range(len(wallpaper) - 1, -1, -1):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                s[1] = min(s[1], j)
    # 끝점 찾기(행)
    for i in range(len(wallpaper) - 1, -1, -1):
        if "#" in wallpaper[i]:
            e[0] = i
            break
    # 끝점 찾기(열)
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                e[1] = max(e[1], j)

    e[0] +=1
    e[1] +=1
    answer.extend(s)
    answer.extend(e)

    return answer