from collections import deque 

def solution(maps):
    m, n = len(maps), len(maps[0])
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    queue = deque([(0,0)])
    maps[0][0] = 2 
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx < m and 0<= ny < n and maps[nx][ny] == 1: 
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx,ny))
                
    return maps[m -1][n-1] - 1 if maps[m-1][n-1] > 1 else -1 
        
