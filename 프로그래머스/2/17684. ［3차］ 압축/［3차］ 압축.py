def solution(msg):
    answer = []
    idx = 1
    words = {}
    msg = msg.upper()
    for i in range(ord('A'), ord('Z') + 1):
        words[chr(i)] = idx
        idx += 1
    tmp = ''
    for i in range(len(msg)):
        tmp += msg[i]

        if tmp not in words.keys():
            w = tmp[:-1]
            c = tmp[-1]
            answer.append(words[w])
            words[tmp] = idx
            idx += 1
            tmp = msg[i]
    answer.append(words[tmp])
    return answer