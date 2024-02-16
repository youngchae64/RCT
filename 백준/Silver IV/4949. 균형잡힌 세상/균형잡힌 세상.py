
while True:
    word = input()

    if word == ".":
        break

    stack = []  # VPS 판정을 위한 스택 선언

    for char in word:
        if char == "(":
            stack.append(char)

        elif char == ")":
            # 스택이 비어있거나 안비어 있는데 마지막이 열린 괄호가 아닐 경우
            if not stack or stack[-1] != "(":
                print("no")
                break
            elif stack[-1] == "(":  # 스택이 차있으면
                stack.pop()

        elif char == "[":
            stack.append(char)

        elif char == "]":
            if not stack or stack[-1] != "[":
                print("no")
                break
            elif stack[-1] == "[":
                stack.pop()

    else:
        if not stack:  # success 변수가 True인 경우에만 "YES" 출력
            print("yes")
        else:
            print("no")
