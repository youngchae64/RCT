import sys

n, m = map(int, input().split())

# 집합 S를 저장할 set 생성
s = set()

for i in range(n):
    word = input()
    s.add(word)

cnt = 0
for j in range(m):
    word = input()
    if word in s:  # 검사해야 하는 문자열이 집합 S에 있는지 확인
        cnt += 1

print(cnt)
