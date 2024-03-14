def solution(dots):
    answer = 0
    arr = []
    # [x1,y1] 과 [x2,y2]
    tan1 = (dots[0][1] - dots[1][1])/(dots[0][0] - dots[1][0])
    arr.append(tan1)
    # [x3,y3] 과 [x4,y4]
    tan2 = (dots[2][1] - dots[3][1])/(dots[2][0] - dots[3][0])
    if tan1 == tan2 :
        return 1
    
    arr.append(tan2)
    # [x1,y1] 과 [x3,y3]
    tan3 = (dots[2][1] - dots[0][1])/(dots[2][0] - dots[0][0])
    arr.append(tan3)
    # [x2,y2] 과 [x4,y4]
    tan4 = (dots[3][1] - dots[1][1])/(dots[3][0] - dots[1][0])
    if tan3 == tan4:
        return  1
    
    arr.append(tan4)
    # [x1,y1] 과 [x4,y4]
    tan5 = (dots[3][1] - dots[0][1])/(dots[3][0] - dots[0][0])
    arr.append(tan5)
    # [x2,y2] 과 [x3,y3]
    tan6 = (dots[1][1] - dots[2][1])/(dots[1][0] - dots[2][0])
    arr.append(tan6)
    if tan5 == tan6:
        return 1
    
    
    return 0