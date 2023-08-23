dot = []

def is_minimum(x,y,w,h):
    
    
    x_length = abs(w-x)
    y_length = abs(h-y)
    
    dot.append(x)
    dot.append(y)
    dot.append(x_length)
    dot.append(y_length)
    
    
    minimum = min(dot)
    
    return minimum

x,y,w,h = map(int,input().split())

minimum = is_minimum(x,y,w,h)
        
print(minimum)