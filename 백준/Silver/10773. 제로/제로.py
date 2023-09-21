import sys

K = int(input())

class Stack():
    def __init__(self):
        self.stack = []
        
    def push(self,x):
        self.stack.append(x)
        
    def is_empty(self):
        if(len(self.stack) == 0):
            return 1
        else:
            return 0 
        
    def pop(self):
        if(self.is_empty()):
            return -1
        else:
            return self.stack.pop()

my_stack = Stack()

output = []  # 결과를 저장할 리스트

for _ in range(K):
    num = int(sys.stdin.readline())
    
    if num == 0:
        my_stack.pop()
    else:
        my_stack.push(num)

while not my_stack.is_empty():
    a = my_stack.pop()
    output.append(a)

print(sum(output))