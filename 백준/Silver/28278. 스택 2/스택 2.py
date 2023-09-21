import sys
input = sys.stdin.readline

N = int(input())

class Stack():
    def __init__(self):
        self.stack = []
    #1   
    def push(self,x):
        self.stack.append(x)
    #4    
    def is_empty(self):
        if(len(self.stack) == 0):
            return 1
        else:
            return 0
      
    #2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
    def pop(self):
        if(self.is_empty()):
            return -1
        else:
            top = self.stack[-1]
            self.stack.pop()
            return top 
    #3    
    def count(self):
        return len(self.stack)
    
    #5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
    def pop1(self):
        if(self.is_empty()):
            return -1
        else:
            top1 = self.stack[-1]
            return top1
        
my_stack = Stack()
            
for _ in range(N):
    command = list(map(int, input().split()))
    
    if (command[0] == 1):
        my_stack.push(int(command[1]))
    elif(command[0] == 2):
        print(my_stack.pop())
    elif(command[0] ==3):
        print(my_stack.count())
    elif(command[0] ==4):
        print(my_stack.is_empty())
    elif(command[0] ==5):
        print(my_stack.pop1())
    