def solution(id_pw, db):
    answer = ''
    for i,j in db:
        if i == id_pw[0] and j == id_pw[1]:
            return "login"
        elif i == id_pw[0] and j != id_pw[1]:
            return "wrong pw"
    return "fail"