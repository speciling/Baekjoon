n = int(input())
arr = list(map(int, input().split()))
max_num = max(arr)
if max_num <= 0:
    print(max_num)
else:
    s = [0] * n
    s[0] = arr[0] if arr[0] >= 0 else 0
    for i in range(1, n):
        s[i] = s[i-1] + arr[i]
        if s[i] < 0:
            s[i] = 0
    print(max(s))