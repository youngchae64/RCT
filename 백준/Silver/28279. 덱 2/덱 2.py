from collections import deque
import sys
input = sys.stdin.readline


class Deque():
    def __init__(self):
        self.deque = deque()

    def one(self, X):
        self.deque.appendleft(X)

    def two(self, X):
        self.deque.append(X)

    def is_empty(self):
        if (len(self.deque) == 0):
            return 1
        else:
            return 0

    def three(self):
        if (self.is_empty()):
            print(-1)
        else:
            a = self.deque.popleft()
            print(a)

    def four(self):
        if (self.is_empty()):
            print(-1)
        else:
            b = self.deque.pop()
            print(b)

    def five(self):
        print(len(self.deque))

    def six(self):
        if (self.is_empty()):
            print(1)
        else:
            print(0)

    def seven(self):
        if (self.is_empty()):
            print(-1)
        else:
            print(self.deque[0])

    def eight(self):
        if (self.is_empty()):
            print(-1)
        else:
            print(self.deque[-1])


N = int(input())

my_queue = Deque()

for _ in range(N):
    command = list(map(int, input().split()))

    if (command[0] == 1):
        my_queue.one(int(command[1]))
    elif (command[0] == 2):
        my_queue.two(command[1])
    elif (command[0] == 3):
        my_queue.three()
    elif (command[0] == 4):
        my_queue.four()
    elif (command[0] == 5):
        my_queue.five()
    elif (command[0] == 6):
        my_queue.six()
    elif (command[0] == 7):
        my_queue.seven()
    elif (command[0] == 8):
        my_queue.eight()
