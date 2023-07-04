N = int(input())

star = "*"
ent = " "
i = 1

while N>0:
    print(ent*(N-1) + star*i)
    i += 1
    N -= 1
    