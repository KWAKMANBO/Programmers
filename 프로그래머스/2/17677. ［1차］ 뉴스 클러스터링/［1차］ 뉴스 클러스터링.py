# 합집합
def union(arr1, arr2):
    answer = []
    cnt = {}

    for i in arr1:
        if i in cnt.keys():
            continue

        if i in arr2:
            cnt[i] = max(arr1.count(i), arr2.count(i))
        else:
            cnt[i] = arr1.count(i)

    for i in arr2:
        if i not in cnt.keys():
            cnt[i] = arr2.count(i)
    for c in cnt:
        answer.extend([c] * cnt[c])
    return answer


# 교집합
def intersection(arr1, arr2):
    cnt = {i: min(arr1.count(i), (arr2.count(i))) if i in arr2 else 0 for i in arr1}
    answer = []
    for c in cnt:
        answer.extend([c] * cnt[c])

    return answer


def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    set1 = []
    set2 = []

    for i in range(0, len(str1) - 1):
        if str1[i:i + 2].isalpha():
            set1.append(str1[i:i + 2])

    for i in range(0, len(str2) - 1):
        if str2[i:i + 2].isalpha():
            set2.append(str2[i:i + 2])

    uni = len(union(set1, set2))
    inter = len(intersection(set1, set2))

    if uni == 0:
        return 65536
    else:
        return int((inter / uni) * 65536)