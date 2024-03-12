def solution(dots):
    x_arr = [dots[i][0] for i in range(len(dots))]
    y_arr = [dots[i][1] for i in range(len(dots))]
    
    return abs(max(x_arr) - min(x_arr))*abs(max(y_arr) - min(y_arr))