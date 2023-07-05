arr = []

for i in range(1,10):
    num = int(input())
    arr.append(num)
    
max_num = max(arr)
print(max_num)

for i in range(0,9):
    if (arr[i] == max_num):
        print(i+1)