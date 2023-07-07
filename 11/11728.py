import sys
sys.stdin.readline()
print(*sorted(sys.stdin.read().split(), key=int))