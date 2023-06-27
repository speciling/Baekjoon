n, m = map(int, input().split())
if n >= 3:
    if m >= 7:
        print(m-2)
    elif 5 <= m <= 6:
        print(4)
    else:
        print(m)
elif n == 2:
    print(min(4, (m-1)//2+1))
else:
    print(1)