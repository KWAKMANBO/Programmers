def solution(a,b,c,d):
    arr = [a,b,c,d]
    count_list = [arr.count(i) for i in arr]
    #count 메서드는 리스트에 존재하는 해당하는 요소의 개수를 카운트 해줌
    
    
    if max(count_list) == 4:
        # 4개의 숫자가 모두 같을 경우
        return a*1111 
    elif max(count_list) == 3:
        # 숫자가 2개 1개 1개 일 경우
        # index메서드는 넣은 인자 값의 첫 인덱스를 반환해줌
        p = arr[count_list.index(3)]
        # count가 3인 요소의 첫 인덱스를 반환 
        q = arr[count_list.index(1)]
        # count가 1인 요소의 첫 인덱스를 반환
        return(10*p + q)**2
    elif max(count_list) == 2:
        if min(count_list)==2:
            # 숫자가 2개 2개인경우
            return (a+c)*abs(a-c) if a == b else (a+b)*abs(a-b)
        else:
            # 숫자가 2개 1개 1개 인경우
            # 4개의 숫자중  p , p , q ,r 이므로
            ## (a*b*c*d)/p**2는 q * r이됨
            p = arr[count_list.index(2)]
            return (a*b*c*d)/p**2
    else:
        return min(arr)
        
            
        
        
    