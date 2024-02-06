N = int(input())
standing = list(map(int, input().split()))
stack = []
target = 1

while standing:
    if standing[0] == target:  # standing에 있는 원소가 target 이면
        standing.pop(0)  # pop하고
        target += 1  # target 원소 증가
    else:
        stack.append(standing.pop(0))  # 새로운 stack에 원소 추가

    while stack:
        if stack[-1] == target:
            stack.pop()
            target += 1
        else:
            break

if not stack:
    print('Nice')
else:
    print('Sad')
