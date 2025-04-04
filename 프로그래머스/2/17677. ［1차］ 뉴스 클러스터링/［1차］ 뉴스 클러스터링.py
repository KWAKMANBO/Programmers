def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    set1 = [str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    set2 = [str2[i:i+2] for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

    union_set = set(set1) | set(set2)
    intersection_set = set(set1) & set(set2)

    multi_union = sum(max(set1.count(u), set2.count(u)) for u in union_set)
    multi_intersection = sum(min(set1.count(i),set2.count(i)) for i in intersection_set)

    if multi_union == 0 and multi_union == 0:
        return 65536
    else:
        return int((multi_intersection/multi_union)*65536 )