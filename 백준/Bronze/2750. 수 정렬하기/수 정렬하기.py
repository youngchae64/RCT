#2750

N = int(input())

stack = []

for i in range(0,N):
    num = int(input())
    stack.append(num)
    
new = sorted(stack)

for _ in range(0,N):
    print(new[_])

