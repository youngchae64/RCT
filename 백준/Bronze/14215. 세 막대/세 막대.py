def tri(arr):
    length = 0
    if arr[0] == arr[1] == arr[2]:
        length = sum(arr)
    else:
        if max_value < other:
            length = sum(arr)
        else:
            length = other + (other - 1)
            
    return length 


N = map(int, input().split())
N = list(N)

max_value = max(N)
other = sum(N) - max_value

length = tri(N)
print(length)
