#2757

N = int(input())

stack = []

for i in range(0,N):
    stack.append(int(input()))
    
new = sorted(stack)

for i in sorted(stack):
    print(i)