import sys

n, k = map(int, input().split())
nums = []

for _ in range(n):
    x = int(input())
    nums.append(x)

nums.sort(reverse=True)
cnt = 0
total = 0
rest = k  # k는 목표금액

for won in nums:
    if won <= rest:  # won이 목표금액보다 크면 건너뜀
        total = rest//won  # 총 필요한 코인갯수
        cnt += total  # 코인갯수 증가
        rest %= won

print(cnt)
