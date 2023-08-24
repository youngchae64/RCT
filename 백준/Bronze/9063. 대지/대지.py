def is_area(N):
    x_matrix = []
    y_matrix = []
    
    for i in range(0,N):
        x,y = map(int,input().split())
        x_matrix.append(x)
        y_matrix.append(y)
            
    x_max = max(x_matrix)
    x_min = min(x_matrix)
    y_max = max(y_matrix)
    y_min = min(y_matrix)
    
    width = x_max - x_min
    height = y_max - y_min 
    
    area = width*height
    
    return area

N = int(input())

if(N>= 2):
    area = is_area(N)
    print(area)
else:
    print("0")