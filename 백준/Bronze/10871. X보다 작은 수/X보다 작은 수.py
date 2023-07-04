N,X = map(int,input().split())
arr = list(map(int,input().split()))
new_arr = []

for i in range(1,N+1):
    if (arr[i-1] < X):
        new_arr.append(arr[i-1])

new_arr_output = ' '.join(map(str,new_arr))
print(new_arr_output)