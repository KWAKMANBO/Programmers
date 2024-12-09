def solution(s, n):
    answer = ''
    for c in s:
        code = ord(c)

        if 64 < code < 91:
            code += n
            if code > 90:
                answer += chr(code - 26)
            else:
                answer += chr(code)
        elif code == 32:
            answer += " "
        else:
            code += n
            if code > 122:
                answer += chr(code - 26)
            else:
                answer += chr(code)
    return answer

