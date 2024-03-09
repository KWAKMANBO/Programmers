def solution(num, k):
    num_str = str(num)
    if str(k) in num_str:
        return num_str.find(str(k)) + 1
    else:
        return -1