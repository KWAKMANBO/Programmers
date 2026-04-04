def solution(message, spoiler_ranges):
    answer = 0
    no_spoiler_ranges = []
    no_spoiler_words = []
    spoiler_words = []
    # no_spoiler_ranges를 담을 떄 사용할 idx
    idx = 0

    # for m in range(len(message)):
    #     print(f"{m} : {message[m]}")

    for i in spoiler_ranges:
        start, end = i[0], i[1]

        # spoiler range의 시작점 찾기
        while True:
            if message[start] == " " or start == 0:
                break
            start -= 1

        while True:
            if message[end] == " " or end == len(message) - 1:
                if end == len(message) - 1:
                    end += 1
                break
            end += 1

        for w in message[start:end].strip().split():
            spoiler_words.append(w)

        if start != 0:
            no_spoiler_ranges.append([idx, start + 1])
        idx = end

    if idx != len(message):
        no_spoiler_ranges.append([idx, len(message)])
    
    for s, e in no_spoiler_ranges:
        tmp = message[s:e].strip().split()
        for t in tmp:
            no_spoiler_words.append(t)

    spoiler_words = set(spoiler_words)
    for sw in spoiler_words:
        if sw not in no_spoiler_words:
            answer += 1
            
    return answer