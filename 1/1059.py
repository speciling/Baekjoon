l = int(input())
s = list(map(int, input().split()))
n = int(input())

if n in s:
    print(0)
else:
    s.sort()
    if n < s[0]:
        print((n-1)*(s[0]-n) + (s[0]-n-1))
    else:
        for i in range(l):
            if s[i] > n:
                print((n - s[i-1] - 1) * (s[i] - n) + (s[i] - n - 1))
                break
