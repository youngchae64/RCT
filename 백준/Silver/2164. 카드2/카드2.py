from collections import deque 

N = int(input())

queue = deque()

for i in range(0,N):
        queue.append(i+1)
       

while (len(queue)>1):
    
    queue.popleft()
    
    if(len(queue) == 1):
        break
        
    top = queue.popleft()
    queue.append(top)
    
 
 
print(queue[0])
        
        
    