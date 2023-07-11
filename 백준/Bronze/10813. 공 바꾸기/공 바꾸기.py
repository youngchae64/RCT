N,M = map(int,input().split())

arr = [0]*N 
k = 1 

for y in range(0,N):
    arr[y] = k
    k += 1

for x in range(1,M+1):
    i,j = map(int,input().split())
    temp = arr[j-1] 
    arr[j-1]  = arr[i-1] 
    arr[i-1] = temp
    
output = ' '.join(str(element) for element in arr)
print(output)