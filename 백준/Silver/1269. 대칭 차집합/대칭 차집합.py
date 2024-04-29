import sys
from collections import Counter

a, b = map(int, input().split())

a_sum = []
a_sum = sys.stdin.readline().rstrip().split()

b_sum = []
b_sum = sys.stdin.readline().rstrip().split()

total = a_sum + b_sum

dictionary = Counter(total)

cnt = 0
for key, value in dictionary.items():
    if value == 1:
        cnt += 1

print(cnt)