def solution(brown, yellow):
    answer = []
    num_tiles = brown + yellow
    for i in range(1, yellow+1):
        if yellow % i == 0:
            h = i
            w = yellow // i
            if 2 * (w + h + 2) == brown:
                print(f"w : {w} , h : {h}")
                return [w+2, h+2]
