def solution(myString, pat):
    str1 =  myString.lower()
    str2 =  pat.lower()
    
    if str1.count(str2) > 0 :
        return 1
    else:
        return 0