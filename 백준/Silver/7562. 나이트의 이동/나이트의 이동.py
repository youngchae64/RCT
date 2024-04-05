from collections import deque
import sys
input = sys.stdin.readline

T = int(input().rstrip())


def bfs():

    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]

    queue = deque([(n_x, n_y)])

    while queue:
        x, y = queue.popleft()
        if (x == a_x and y == a_y):
            return visited[x][y] - 1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < l and 0 <= ny < l) and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))


for i in range(0, T):
    l = int(input())
    n_x, n_y = map(int, input().split())
    a_x, a_y = map(int, input().split())
    visited = [[0]*l for _ in range(l)]
    visited[n_x][n_y] = 1
    print(bfs())
