N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)

cnt = 1
number = 0
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, start, visited):
    global cnt
    global number

    visited[start] = cnt

    for i in graph[start]:
        if visited[i] == 0:
            number += 1
            dfs(graph, i, visited)


dfs(graph, 1, visited)
print(number)
