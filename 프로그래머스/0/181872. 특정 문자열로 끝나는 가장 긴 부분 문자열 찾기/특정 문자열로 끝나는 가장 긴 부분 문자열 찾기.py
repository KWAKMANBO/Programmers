def solution(myString, pat):
    answer = myString
    while True:
        if not answer.endswith(pat):
            answer = answer[:len(answer)-1]
        else:
            return answer