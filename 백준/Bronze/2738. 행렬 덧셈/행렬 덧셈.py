N, M = map(int, input().split())

matrix_A = []
matrix_B = []

# 행렬 A 입력 받기
for i in range(N):
    row = list(map(int, input().split()))
    matrix_A.append(row)

# 행렬 B 입력 받기
for i in range(N):
    row = list(map(int, input().split()))
    matrix_B.append(row)

# 행렬 A와 B를 더한 결과 출력
result_matrix = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(matrix_A[i][j] + matrix_B[i][j])
    result_matrix.append(row)

# 결과 행렬 출력
for row in result_matrix:
    print(*row)
