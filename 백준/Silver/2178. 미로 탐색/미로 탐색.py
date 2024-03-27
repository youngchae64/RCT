from collections import deque

# 입력받은 미로의 크기 N(행), M(열)
N, M = map(int, input().split())

graph = []

# 미로 정보를 입력받아 2차원 리스트로 구성
for _ in range(N):
    graph.append(list(map(int, input())))


def bfs(x, y):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()

    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))  # 해당 위치를 기반으로 주변을 다시 탐색할 준비를 하는 과정

    return graph[N-1][M-1]


print(bfs(0, 0))
