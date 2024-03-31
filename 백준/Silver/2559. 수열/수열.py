from collections import deque
import sys
input = sys.stdin.readline

# 10, 2 일때
n, k = map(int, input().split())  # n은 온도 측정한 전체 날의 수, k는 합을 구하기 위한 연속적인 날짜수

temperatures = list(map(int, input().split()))

# 초기 슬라이딩 윈도우의 합을 계산합니다.
current_sum = sum(temperatures[:k])
# 결과 리스트에 첫 번째 윈도우의 합을 추가합니다.
result = [current_sum]

# 슬라이딩 윈도우를 이용하여 나머지 합을 계산합니다.
for i in range(1, n - k + 1):
    # 새 윈도우의 합을 업데이트합니다: 이전 윈도우의 합에서 가장 왼쪽 값을 빼고, 새로운 오른쪽 값을 더합니다.
    current_sum = current_sum - temperatures[i - 1] + temperatures[i + k - 1]
    result.append(current_sum)

result.sort(reverse=True)

print(result[0])
