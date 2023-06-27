n, k = map(int, input().split())
arr = list(map(int, input().split()))

plug = []
cnt = 0
for i in range(k):
    if arr[i] not in plug:
        if len(plug)<n:
            plug.append(arr[i])
            continue
        x, max_idx = 0, -1
        for j in range(n):
            try:
                idx = arr[i:].index(plug[j])
                if idx > max_idx:
                    x = j
                    max_idx = idx
            except:
                x = j
                break
        plug[x] = arr[i]
        cnt += 1
print(cnt)