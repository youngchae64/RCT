def melody_as(array):
    sum = 0 
    for i in range(0,8):
        if(array[i] == (i+1)):
            sum += 1
    return sum 
        
def melody_ds(array):
    sum_ds = 1
    for i in range(0,8):
        if(array[i] == (8-i)):
             sum_ds += 1
    return sum_ds

        
N = list(map(int,input().split()))
array = []
array.append(N)

result_as = melody_as(N)
result_ds = melody_ds(N)

if(result_as == 8):
    print("ascending")
elif(result_ds == 9):
    print("descending")
else:
    print("mixed")
