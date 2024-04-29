import sys
from collections import Counter

n, m = map(int, input().split())
total = n+m
name_heardseen = []

for i in range(total):
    name = input()
    name_heardseen.append(name)

dictionary = Counter(name_heardseen)

answer = []

for key, value in dictionary.items():
    if value == 2:
        answer.append(key)

answer.sort()
print(len(answer))
for element in answer:
    print(element, end='\n')
