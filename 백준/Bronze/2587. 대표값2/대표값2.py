#2578

stack = []

for i in range(0,5):
    num = int(input())
    stack.append(num)
    
new = sorted(stack)

center = new[2]
mean = sum(new)/5

print(int(mean))
print(center)