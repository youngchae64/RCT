#11022
T = int(input())

x = 1
while T>0: 
    A,B = map(int,input().split())
    print(f"Case #{x}: {A} + {B} = {A+B}")
    T -= 1
    x += 1 