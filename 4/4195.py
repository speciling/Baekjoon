from sys import stdin
input = stdin.readline

def solve():
    root = {}

    def findroot(node):
        if node not in root:
            root[node] = 1
            return node
        elif type(root[node]) == int:
            return node
        else:
            root[node] = findroot(root[node])
            return root[node]

    def union(r1, r2):
        root[r1] += root[r2]
        root[r2] = r1

    for _ in range(int(input())):
        name1, name2 = input().split()
        root1, root2 = findroot(name1), findroot(name2)
        if root1 != root2:
            union(root1, root2)
        print(root[root1])


for t in range(int(input())):
    solve()

