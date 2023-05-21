n = int(input())
files = list(map(int, input().split()))
c = int(input())
ans = 0
for file in files:
    ans += file - file % c + c if file % c else file
print(ans)