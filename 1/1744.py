import sys
input = sys.stdin.readline

pn, nn = [], []  # 양수, 음수(0포함) 리스트
ans = 0

for _ in range(int(input())):
    n = int(input())
    if n > 1:
        pn.append(n)
    elif n == 1:
        ans += 1
    else:
        nn.append(n)
pn.sort(reverse=True)
nn.sort()

if len(nn)%2:
    ans += nn.pop()
while nn:
    ans += nn.pop()*nn.pop()
if len(pn)%2:
    ans += pn.pop()
while pn:
    ans += pn.pop()*pn.pop()
print(ans)