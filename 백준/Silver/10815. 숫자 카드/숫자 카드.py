import sys

n = int(input())

nums = []
nums = sys.stdin.readline().rstrip().split()

m = int(input())

arr = []

arr = sys.stdin.readline().rstrip().split()

dictionary = {}

for i in arr:
    dictionary[i] = 0

for j in nums:
    if j in dictionary:
        dictionary[j] = 1

for element in dictionary:
    print(dictionary[element], end=' ')