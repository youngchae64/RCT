import sys 

T = int(input())

C = 1 
while T>0: 
    A,B = map(int,sys.stdin.readline().split())
    print(f"Case #{C}: {A+B}")
    T -= 1 
    C += 1
    