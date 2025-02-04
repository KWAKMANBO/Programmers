def solution(n):
    answer = 0
    cnt = bin(n)[2:].count("1")
    i = n
    while True:
        i += 1
        bin_i = bin(i)[2:]
        if bin_i.count("1") == cnt and int(bin_i, 2) > n:
            return i
