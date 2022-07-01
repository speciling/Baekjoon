from sys import stdin

n = int(input())
nums = list(set(map(int, stdin.readline().split())))
print(*sorted(nums))