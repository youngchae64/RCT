A,B = input().split()

A_r = A[::-1]
B_r = B[::-1]

if(A_r>B_r):
    print(A_r)
else:
    print(B_r)