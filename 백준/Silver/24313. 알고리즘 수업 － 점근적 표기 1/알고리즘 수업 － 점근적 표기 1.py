a1, a2 = map(int, input().split())

c = int(input())
n = int(input())

x = n

fn = a1*x + a2
gn = c*x

if fn <= gn and a1 <= c:
    print(1)
else:
    print(0)
