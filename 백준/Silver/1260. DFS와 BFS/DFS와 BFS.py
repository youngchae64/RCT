#1260 

import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

#정점갯수, 간선갯수, 시작노드 
n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited_bfs = [0]*(n+1)
visited_dfs = [0]*(n+1)

c = 1
got = 1 

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a) 

for i in range(n+1): #인접노드는 오름차순 방문한다고 했으므로 오름차순 정렬  
    graph[i].sort()


def bfs(graph,start,visited_bfs):
    global c 
    
    queue = deque([start]) #큐 정의와 초기화 
    
    visited_bfs[start] = c #bfs에서 방문한 노드 visited_bfs를 1로 변경 
    
    while queue: #
        
        v = queue.popleft() #원소꺼내서 
        print(v, end =' ') #출력 
        
        for i in graph[v]: #노드 v와 인접한 노드들에 대해 
            if visited_bfs[i] == 0: # 아직 방문하지 않았다면 
                queue.append(i) #큐에 추가하고 
                visited_bfs[i] = c # visited_bfs를 1로 변경 
                

def dfs(graph, start, visited_dfs):
    
    global got
    
    visited_dfs[start] = got #시작노드 1에 추가 
    print(start, end =' ')
    
    for i in graph[start]:
        if visited_dfs[i] == 0:
            dfs(graph,i,visited_dfs) 
    
    
dfs(graph,v,visited_dfs)
print()
bfs(graph,v,visited_bfs) 