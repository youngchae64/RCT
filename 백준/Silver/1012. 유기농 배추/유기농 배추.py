import sys
from collections import deque
sys.setrecursionlimit(10000) 

input = sys.stdin.readline


T = int(input())

graph = []
count = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    global count

    if x < 0 or x >= M or y < 0 or y >= N:
        return

    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)


for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(N)] for _ in range(M)]
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a][b] = 1

    result = []
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                dfs(i, j)
                result.append(count)
                count = 0

    print(len(result))
