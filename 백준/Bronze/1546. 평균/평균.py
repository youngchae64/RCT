N = int(input())
arr = list(map(int,input().split()))

M = max(arr)

for i in range(0,N):
    arr[i] = (arr[i]/M*100)
    
avg = sum(arr)/len(arr)
print(avg)