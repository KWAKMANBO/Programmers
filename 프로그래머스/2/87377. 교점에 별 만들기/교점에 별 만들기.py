def solution(line):
    
    points = set()
    ln = len(line)
    for i in range(ln - 1):
        a, b, c = line[i]
        for j in range(i + 1, ln):
            d, e, f = line[j]

            divisor = a * e - b * d

            if divisor == 0:
                continue
            num_x = b * f - c * e
            num_y = c * d - a * f
            if num_x % divisor == 0 and num_y % divisor == 0:
                points.add(((b * f - c * e) // divisor, (c * d - a * f) // divisor))

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    max_x, min_x = max(xs), min(xs)
    max_y, min_y = max(ys), min(ys)

    lst = [["." for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]

    for x, y in points:
        r = max_y - y
        c = x - min_x
        lst[r][c] = "*"

    return ["".join(l) for l in lst]