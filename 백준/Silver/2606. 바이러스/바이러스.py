#2606 
import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

number = int(input())
edge = int(input())
graph = [[] for _ in range(number+1)]
visited = [0]*(number +1) # 방문할 노드 

for i in range(edge):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
c = 1     
def bfs(graph, start, visited):
    global c 
    
    visited[start] = c 
    
    queue = deque([start]) 
    
    
    while queue:
        
        v = queue.popleft()
        
        for i in graph[v]:
            if visited[i] ==0:
                queue.append(i)
                visited[i] = c 
                
bfs(graph,1,visited)

cnt = 0 

for i in range(1,number+1):
    if visited[i] ==1:
        cnt += 1 

if (cnt>=1):
    cnt = cnt - 1
        
print(cnt)