from collections import deque

def solution(s):
    
    queue = deque()
    
    for i in s:
        if i == "(":
            queue.append(i)
        else: #s의 원소가 ")" 일때 
            if not queue: #큐가 비어있을때 
                return False 
            else:
                queue.pop()
                
    if not queue:
        return True
    else:
        return False
                
    
    
    