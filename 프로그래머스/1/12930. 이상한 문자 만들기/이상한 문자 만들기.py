def solution(s):
    words = []
    answer = ''
    for word in s.split(" "):
        tmp = ""
        for idx in range(len(word)):
            if idx % 2 == 0:
                tmp += word[idx].upper()
            else:
                tmp += word[idx].lower()
        words.append(tmp)
    return " ".join(words)