import sys
from collections import Counter

n = int(input())
nums = []
nums = sys.stdin.readline().rstrip().split()

m = int(input())
arr = []
arr = sys.stdin.readline().rstrip().split()

dictionary = Counter(nums)


answer = []

for element in arr:
    if element in dictionary.keys():
        answer.append(dictionary[element])
    else:
        answer.append(0)

print(' '.join(map(str, answer)))
