import sys 

while(1):
    x,y = map(int,input().split())
    
    if(x==y):
        sys.exit()
    else:
        if((y%x) == 0):
            print("factor")
        else:
            if((x%y) == 0):
                print("multiple")
            else:
                print("neither")