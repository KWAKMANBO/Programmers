def solution(s):
    answer = 0
    for i in range(-1,len(s)-1):
        tmp = s[i+1:]+s[:i+1]
        stack = []
        cnt = 0
        for t in tmp:
            # print(stack)
            if t == "[" or t == "{" or t == "(":
                stack.append(t)
                cnt +=1

            if stack and stack[-1] == "[" and t == "]":
                stack.pop()
                cnt +=1
            elif stack and stack[-1] == "{" and t == "}":
                stack.pop()
                cnt +=1
            elif stack and stack[-1] == "(" and t == ")":
                stack.pop()
                cnt +=1

        if not stack and cnt > 0:
            answer +=1

    return answer