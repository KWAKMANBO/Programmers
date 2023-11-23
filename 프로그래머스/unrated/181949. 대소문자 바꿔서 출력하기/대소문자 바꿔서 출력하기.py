str = input()
result = ""

#ord(문자) -> 문자 하나를 입력받아 해당 유니코드 정수로 반환해주는 메서드

# chr(정수) -> 정수를 인자로 받아서 해당하는 유니코드 문자를 반환해주는 메서드 

for i in range(len(str)):
    if( ord(str[i]) >= 65 and ord(str[i]) <= 90 ) :
       result += chr(ord(str[i]) + 32)
    elif(ord(str[i]) >= 97 and ord(str[i]) <= 122) :
       result += chr(ord(str[i]) - 32)
    else :
        result += str[i]
        
#파이썬에는 swapcase() 메서드가 구현되어 있음 이를 사용해도됨 
        
        
        
print(result)