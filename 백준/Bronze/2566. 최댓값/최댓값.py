# 행렬 입력 받기
matrix = []
max_row = 0
max_column = 0
max_value = 0 

for i in range(9):
    row =  list(map(int, input().split()))
    matrix.append(row)

# 최댓값 찾기
for i, row in enumerate(matrix):
    for j, value in enumerate(row):
        if value > max_value:
            max_value = value
            max_row = i
            max_column = j

max_row += 1 
max_column += 1 

print(max_value)
print(max_row, max_column)
