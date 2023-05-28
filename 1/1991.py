import sys
input = sys.stdin.readline
print = sys.stdout.write


def preorder():
    stk = ['A']
    res = []
    while stk:
        if (now:=stk.pop()) == '.':
            continue
        res.append(now)
        stk += children[now][::-1]
    print(''.join(res))


def inorder(parent):
    if parent == '.':
        return
    inorder(children[parent][0])
    print(parent)
    inorder(children[parent][1])


def postorder(parent):
    if parent == '.':
        return
    postorder(children[parent][0])
    postorder(children[parent][1])
    print(parent)


children = {}
for i in range(n:=int(input())):
    p, c1, c2 = input().split()
    children[p] = [c1, c2]

preorder()
print('\n')
inorder('A')
print('\n')
postorder('A')