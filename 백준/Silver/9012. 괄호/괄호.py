T = int(input())

for _ in range(T):
    word = input()
    stack = []  # VPS 판정을 위한 스택 선언

    for char in word:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack: #스택이 비어있으면 
                print("NO")
                break
            else: #스택이 차있으면 
                stack.pop()
                
    else:
        if not stack:  # success 변수가 True인 경우에만 "YES" 출력
            print("YES")
        else:
            print("NO")
