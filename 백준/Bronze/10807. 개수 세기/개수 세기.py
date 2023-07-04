N = int(input())
arr = list(map(int, input().split()))
v = int(input())
count = 0 

for i in range(1,N+1):
    if (arr[i-1] == v):
        count += 1 
        
print(count)