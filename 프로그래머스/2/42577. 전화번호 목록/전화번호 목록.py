def solution(phone_book):
    hash_map = {}
    
    for i in phone_book:
        hash_map[i] = 1
        
    for i in phone_book:
        arr = ""
        for j in range(len(i)):
            arr += i[j]
            if arr in hash_map and arr != i:
                return False
            
    return True
    
    