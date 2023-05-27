from sys import stdout
print = stdout.write

n, m = map(int, input().split())
nums = input().split()
nums.sort(key=int)

res = [None]*m

def dfs(start, depth):
    if depth == m:
        print(' '.join(res) + '\n')
        return
    before = ''
    for i in range(start, n):
        if before != nums[i]:
            res[depth] = nums[i]
            dfs(i+1, depth+1)
            before = nums[i]

dfs(0, 0)