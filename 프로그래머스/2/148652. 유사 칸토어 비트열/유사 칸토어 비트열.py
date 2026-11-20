def solution(n, l, r):

    def dfs(n, sectionStart, l, r):
        length = 5 ** n
        sectionEnd = sectionStart + length - 1

        if sectionEnd < l or sectionStart > r:
            return 0

        if l <= sectionStart and sectionEnd <= r:
            return 4 ** n

        if n == 0:
            return 1

        nextSectionSize = length // 5
        result = 0

        for i in range(5):
            if i == 2:
                continue

            nextSectionStart = sectionStart + i * nextSectionSize
            result += dfs(n - 1, nextSectionStart, l, r)
        return result


    return dfs(n,1,l,r)