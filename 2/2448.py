from sys import stdout
print = stdout.write


def draw(n, res):
    if n == 3:
        return
    draw(n//2, res)
    a = len(res[-1])
    tmp = [line.ljust(a)+line for line in res]
    res += tmp


ans = ["*", "* *", "***** "]
n = int(input())
draw(n, ans)
for i in ans:
    print(i.center(2*n) + "\n")