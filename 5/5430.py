from sys import stdin
from collections import deque
input = stdin.readline

for _ in range(int(input())):
    funcs = input()
    if int(input()):
        arr = deque(input()[1:-2].split(","))
    else:
        input()
        arr = deque()
    isreversed = False
    for func in funcs:
        if func == "R":
            isreversed = not isreversed
        elif func == "D":
            if not arr:
                print("error")
                break
            elif isreversed:
                arr.pop()
            else:
                arr.popleft()
    else:
        if isreversed:
            arr.reverse()
        print("["+",".join(arr)+"]")

