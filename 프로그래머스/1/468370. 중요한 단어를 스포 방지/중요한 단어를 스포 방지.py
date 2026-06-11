def solution(message, spoiler_ranges):
    answer = 0
    spoiler_words = []
    no_spoiler_range = []
    idx = 0
    for sp in spoiler_ranges:
        s, e = sp[0], sp[1]
        while 0 < s and message[s] != " ":
            s -= 1
        while e < len(message) and message[e] != " ":
            e += 1
        # print(f"s: {s}, e: {e}")
        w = message[s:e]
        # print(w.split())
        spoiler_words.extend(w.split())

        if s != 0:
            no_spoiler_range.append([idx, s + 1])
        idx = e

    if idx != len(message):
        no_spoiler_range.append([idx, len(message)])

    no_spoiler_words = []
    for s, e, in no_spoiler_range:
        tmp = message[s:e].split()
        for t in tmp:
            no_spoiler_words.append(t)


    spoiler_words = set(spoiler_words)
    for sw in spoiler_words:
        if sw not in no_spoiler_words:
            answer += 1
    return answer