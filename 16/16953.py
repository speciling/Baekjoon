a, b = map(int, input().split())
cnt = 1
while a < b:
    if not b%2:
        b //= 2
    elif b%10 == 1:
        b //= 10
    else:
        break
    cnt += 1
print(cnt if a==b else -1)