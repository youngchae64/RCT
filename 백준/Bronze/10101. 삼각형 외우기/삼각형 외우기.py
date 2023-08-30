def same_tri(arr):
    total_sum = 0 
    total_sum = arr[0] + arr[1] + arr[2]
    if((total_sum == 180)&((arr[0] == 60)&(arr[1] == 60)&(arr[2] == 60))):
        return 1
    
def tri_iso(arr):
    total_sum = 0 
    total_sum = arr[0] + arr[1] + arr[2]
    if((total_sum == 180)&((arr[0]==arr[1])|(arr[0] == arr[2])|(arr[1] == arr[2]))):
        return 1 
    
def tri_sca(arr):
    total_sum = 0 
    total_sum = arr[0] + arr[1] + arr[2]
    if((total_sum ==180)&((arr[0]!=arr[1])|(arr[0] != arr[2])|(arr[1] != arr[2]))):
        return 1 
    


array = []

for i in range(3):
    N = int(input())
    array.append(N)


if(same_tri(array) == 1):
    print("Equilateral")
elif(tri_iso(array) == 1):
    print("Isosceles")
elif(tri_sca(array) == 1):
    print("Scalene")
else:
    print("Error")