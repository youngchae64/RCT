a,b,c,d,e,f = list(map(int,input().split()))

#x = 1 
#y = 1 

#a*x + b*y = c
#d*x + e*y = f 
#n

#(a-d)x = c-e 
#(b-e)y = c-e 
#x안에 y문 하나씩 증가시켜가면서 위 수식이 일치하는지 확인 
for x in range(-999,1000):
    for y in range(-999,1000):
        if((a*x + b*y == c) and (d*x + e*y == f)):
            print(x,y)