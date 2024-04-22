import sys

n, m = map(int, sys.stdin.readline().split())

id = {}
name = {}


for i in range(1, n+1):
    poketmon = sys.stdin.readline().strip()
    id[i] = poketmon
    name[poketmon] = i


for j in range(m):
    find = sys.stdin.readline().strip()

    if find.isdigit() == True:
        print(id[int(find)])
    else:
        print(name[find])
