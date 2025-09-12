def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):
        tmp = ""
        pat = s[0:i]
        cnt = 1
        for j in range(i, len(s), i):
            if pat == s[j:j + i]:
                cnt += 1
            else:
                tmp += str(cnt) + pat if cnt > 1 else pat
                pat = s[j:j + i]
                cnt = 1
        tmp += str(cnt)+pat if cnt > 1 else pat

        answer = min(answer, len(tmp))

    return answer

# print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))