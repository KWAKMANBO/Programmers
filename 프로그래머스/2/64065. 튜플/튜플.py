def solution(s):
    tuples = []
    i = 0
    s = s[1:-1]
    tmp = ""
    while i < len(s):
        if s[i] == "{":
            i+=1
            continue
        elif s[i] != "}":
            tmp += s[i]
        else:
            tuples.append(list(map(int,tmp.split(","))))
            tmp =""
            i+=1
        i+=1
    tuples.sort(key= lambda x : len(x))
    answer_set = set()
    answer = []
    for t in tuples:
        for i in t:
            if i not in answer_set:
                answer.append(i)
                answer_set.add(i)


    return answer