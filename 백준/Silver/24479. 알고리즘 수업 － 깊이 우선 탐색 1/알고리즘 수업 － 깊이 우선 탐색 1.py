import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

#정점의 수, 간선의 수, 시작정점 
n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)] #0번 인덱스는 무시 
visited = [0]*(n+1) #방문 순서 저장, 0이면 방문 안함 

c = 1 #방문순서 count 할 변수 

def dfs(graph, v, visited):
    global c 
    visited[v] = c # 방문순서 나타내는 코드 
    
    for i in graph[v]: #1번 노드부터 dfs로 인접노드 방문하면서 해당 노드에 방문했으면 방문 순서 기록 
        if visited[i] == 0: #방문안한 노드면 
            c+= 1 # +1하고 
            dfs(graph, i, visited) #재귀함수 호출 
            
for i in range(m): #간선정보 입력받는 부분 
    a,b = map(int,input().split())
    graph[a].append(b) #위에서 초기화한 그래프에 간선정보 추가 
    graph[b].append(a)
    
for i in range(n+1): #인접노드는 오름차순 방문한다고 했으므로 오름차순 정렬  
    graph[i].sort()
    
dfs(graph, r , visited)

for i in range(1,n+1):
    print(visited[i])
    