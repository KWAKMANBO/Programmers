def solution(ineq, eq, n, m):
    Ascii_ineq = ord(ineq)
    Ascii_eq = ord(eq)
    
    sum = Ascii_ineq + Ascii_eq
    # '<' = 60
    # '=' = 61
    # '>' = 62
    # '!' = 33
    # '<=' = 60 + 61 = 121
    # '>=' = 62 + 61 = 123
    # '<!' = 60 + 33 = 93
    # '>!' = 62 + 33 = 95
    
    if sum == 121:
        return int(n <= m)
    elif sum == 123:
        return int(n >= m)
    elif sum == 93:
        return int(n < m)
    else:
        return int(n > m)
    