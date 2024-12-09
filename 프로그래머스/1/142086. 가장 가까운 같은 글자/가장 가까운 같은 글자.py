def solution(s):
    s = s[::-1]
    answer = []
    for i in range(len(s)):
        for j in range(i + 1, len(s)+1):
            if s[i] not in s[j:]:
                answer.append(-1)
                break
            if s[i] == s[j]:
                answer.append(j - i)
                break
    return answer[::-1]