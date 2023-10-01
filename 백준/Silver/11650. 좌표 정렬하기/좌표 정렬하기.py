N = int(input())

coordinates = []

for i in range(N):
    x, y = map(int, input().split())
    coordinates.append((x, y))

# 좌표를 x값을 기준으로 정렬하고, x값이 같을 경우 y값을 기준으로 정렬합니다.
sorted_coordinates = sorted(coordinates, key=lambda coord: (coord[0], coord[1]))

for x, y in sorted_coordinates:
    print(x, y)
