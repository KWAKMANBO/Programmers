def solution(cacheSize, cities):
    answer = 0
    cache = []

    if cacheSize == 0:
        return 5*len(cities)

    for c in cities:
        cc = c.lower()
        if not cc in cache:
            answer += 5
            if len(cache) == cacheSize:
                cache.pop(0)
                cache.append(cc)
            elif len(cache) < cacheSize:
                cache.append(cc)
        else:
            answer += 1
            cache.append(cache.pop(cache.index(cc)))

    return answer