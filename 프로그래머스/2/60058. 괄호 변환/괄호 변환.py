def solution(p):
    answer = ''

    # 올바른 문자열인지 확인하기
    def check(par):

        stack = []
        for i in par:
            if stack and i == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)

        return not stack

    # 주어진 문자열을 u,v로 분리
    def split(w):
        open_cnt = 0
        close_cnt = 0
        for i in range(len(w)):
            if w[i] == "(":
                open_cnt += 1
            else:
                close_cnt += 1
            if open_cnt == close_cnt:
                return w[:i + 1], w[i + 1:]

    def recursive(w):
        # 빈 문자열 이면, 빈 문자열을 반환
        if w == "":
            return ""

        u, v = split(w)

        if check(u):
            return u + recursive(v)
        else:
            u = u[1:-1]
            new_u = ""
            for i in u:
                if i == "(":
                    new_u += ")"
                else:
                    new_u += "("
            return "(" + recursive(v) + ")" + new_u

    return recursive(p)