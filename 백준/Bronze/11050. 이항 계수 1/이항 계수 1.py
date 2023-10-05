#11050 

N,k = map(int,input().split())

total = 1
output = 1 
num = 1 
result = 1

for i in range(1,N+1):
    output *= i 
    

for j in range(1, k+1):
    num *= j 
    
for k in range(1, (N-k+1)):
    result *= k 
    

total = (output)/(num*result)

print(int(total))
    

