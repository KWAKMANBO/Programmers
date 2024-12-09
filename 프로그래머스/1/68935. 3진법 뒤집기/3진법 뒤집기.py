def solution(n):
    ternary = ""
    while n >= 3:
        ternary += str(n % 3)
        n //= 3
    ternary += str(n)
    ternary = ternary[::-1]
    answer = 0
    for i in range(len(ternary)):
        answer += int(ternary[i])*(3**i)
    return answer