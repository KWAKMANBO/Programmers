def solution(s):
    answer = 1000
    if len(s) == 1:
        return  1
    # 1000*1000 O(N^2) == 1000000 백만번? -> 구현 ok
    for i in range(1, len(s) // 2 + 1):
        token = s[0:i]
        token_idx = f"s[0:{i}]"
        tmp = ""
        cnt = 1
        rest = s[len(s) - i: i]
        for j in range(i, len(s), i):
            #print(f"token: {token}, s[{j}:{j + i}] : {s[j:j + i]}, token_idx : {token_idx}, cnt : {cnt}, tmp : {tmp}")
            if token == s[j:j + i]:
                cnt += 1
            else:
                tmp += str(cnt) + token if cnt > 1 else token
                token = s[j:j + i]
                token_idx = f"s[{j}:{j + i}]"
                cnt = 1
            #print(f"token: {token}, s[{j}:{j + i}] : {s[j:j + i]}, token_idx : {token_idx}, cnt : {cnt}, tmp : {tmp}")
            #print()
        tmp += str(cnt) + token if cnt > 1 else token
        answer = min(len(tmp), answer)


    return answer