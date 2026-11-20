import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
dq = deque()

for _ in range(n):
    command = list(map(int, input().split()))
    cmd = command[0]

    if cmd == 1:
        dq.appendleft(command[1])
    elif cmd == 2:
        dq.append(command[1])
    elif cmd == 3:
        print(dq.popleft() if dq else -1)
    elif cmd == 4:
        print(dq.pop() if dq else -1)
    elif cmd == 5:
        print(len(dq))
    elif cmd == 6:
        print(0 if dq else 1)
    elif cmd == 7:
        print(dq[0] if dq else -1)
    elif cmd == 8:
        print(dq[-1] if dq else -1)