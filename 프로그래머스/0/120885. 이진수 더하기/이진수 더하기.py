def solution(bin1, bin2):
    str_b1 = "0b"+str(bin1)
    str_b2 = "0b"+str(bin2)
    num1 = int(str_b1,2)
    num2 = int(str_b2,2)
    return bin(num1+num2)[2:]