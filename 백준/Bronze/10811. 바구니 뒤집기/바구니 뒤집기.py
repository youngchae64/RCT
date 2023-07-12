N,M = map(int,input().split())

arr = []

for x in range(1,N+1):
    arr.append(x)
    
for y in range(1,M+1):
    i,j = map(int,input().split())
    s_point = i-1
    e_point = j
    arr[s_point:e_point] = arr[s_point:e_point][::-1]
    
output = ' '.join(str(element) for element in arr)
print(output)