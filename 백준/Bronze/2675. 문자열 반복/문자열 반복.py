T = int(input())

for i in range(1,T+1):
    R,S = list(input().split())
    new_R = int(R)
    
    for x in range(0,len(S)):
        print(S[x]*new_R, end='')
    print()
