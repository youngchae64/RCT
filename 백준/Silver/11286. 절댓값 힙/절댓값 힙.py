import sys
import heapq as hq

n = int(input())

heap = []

for i in range(n):
    x = int(sys.stdin.readline())

    if x != 0:
        hq.heappush(heap, (abs(x), x))
    else:
        if len(heap) >= 1:
            print(hq.heappop(heap)[1])
        else:
            print(0)
