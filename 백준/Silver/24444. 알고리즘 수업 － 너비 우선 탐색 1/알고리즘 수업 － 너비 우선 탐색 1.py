#24444
import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

#정점, 간선, 시작 
n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

c = 1

#그래프, 시작노드, 방문
def bfs(graph,start, visited):
    
    global c 
    
    queue = deque([start]) #큐 선언 
    
    visited[start] = c #방문순서 나타내는 코드 
    
    while queue:
        
        v = queue.popleft()
        
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                c += 1 
                visited[i] = c 
            
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(n+1):   
    graph[i].sort()
    
bfs(graph, r , visited) 

for i in range(1,n+1):
    print(visited[i])
    