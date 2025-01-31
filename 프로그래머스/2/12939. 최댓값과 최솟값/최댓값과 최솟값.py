def solution(s):
    answer = ''
    lst = list(map(int, s.split()))

    return f"{min(lst)} {max(lst)}"
