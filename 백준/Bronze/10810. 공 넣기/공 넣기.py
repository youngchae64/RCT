N,M = map(int,input().split())

arr = [0]*N

for x in range(1,M+1):
    i,j,k = map(int,input().split())  
    for y in range(i,(j+1)): 
        arr[(y-1)] = k 
        
output = ' '.join(str(element) for element in arr)
print(output)
        