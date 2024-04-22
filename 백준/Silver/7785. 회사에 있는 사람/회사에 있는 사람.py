import sys


n = int(input())
company = {}

for i in range(n):
    person, state = map(str, sys.stdin.readline().split())
    if state == "enter":
        company[person] = True
    else:
        del company[person]

print("\n".join(sorted(company.keys(), reverse=True)))
