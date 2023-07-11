arr = []
divide_arr =[]

for i in range(0,10):
    n = int(input())
    arr.append(n) 


for i in range(0,10):
    divide_arr.append((arr[i])%42)
    
unique_arr = set(divide_arr)
print(len(unique_arr))