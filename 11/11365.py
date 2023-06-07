import sys
while True:
    s = sys.stdin.readline().rstrip()
    if s == "END":
        break
    print(s[::-1])