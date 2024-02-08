import sys
from collections import deque

N, K = map(int, input().split())

queue = deque()
result = []

for i in range(1, N+1):
    queue.append(i)

# 1 2 3 4 5 6 7

# 4 5 6 7 1 2

while queue:  # 큐가 비어있을 때까지 반복
    for _ in range(K-1):
        queue.append(queue.popleft())  # (K-1) 번째까지의 원소를 왼쪽으로 회전시킴

    result.append(queue.popleft())  # 결과적으로 result에 k번째 숫자를 append

print("<", end='')
print(', '.join(map(str, result)), end='')
print(">")
