import sys
input = sys.stdin.readline

sentence = input()
q = int(input())


def numofalpha(a, l, r):
    slicing = sentence[l:r+1]
    cnt = 0
    for j in slicing:
        if (j == a):
            cnt += 1

    return cnt


for i in range(0, q):
    a, l, r = input().split()
    l = int(l)
    r = int(r)
    print(numofalpha(a, l, r))
