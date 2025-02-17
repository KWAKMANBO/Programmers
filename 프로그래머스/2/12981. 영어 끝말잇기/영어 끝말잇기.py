def solution(n, words):
    answer = [0, 0]
    checks = set()
    checks.add(words[0])
    for i in range(1,len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in checks:
            return [i % n + 1, i // n + 1]
        checks.add(words[i])
    return [0, 0]