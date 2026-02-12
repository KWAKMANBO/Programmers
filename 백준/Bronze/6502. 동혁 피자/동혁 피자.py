count = 1
while True:
    info = input().strip()
    if info == '0':
        break

    r, w, l = map(int, info.split())
    if w ** 2 + l ** 2 > (2 * r) ** 2:
        print(f"Pizza {count} does not fit on the table.")
    else:
        print(f"Pizza {count} fits on the table.")
    count += 1
