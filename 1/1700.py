n, k = map(int, input().split())
arr = list(map(int, input().split()))
m = []
ml = 0
count = 0
if n == k:
    print(0)
else:
    for i in range(len(arr)):
        if arr[i] in m:
            continue
        else:
            if ml < n:
                m.append(arr[i])
                ml += 1
            else:
                for j in m:
                    if j not in arr[i:]:
                        m.remove(j)
                        count += 1
                        m.append(arr[i])
                        break
                else:
                    x = 0
                    for j in m:
                        y = arr[i+1:].index(j)
                        x = max(y, x)
                    m.remove(arr[x+i+1])
                    count += 1
                    m.append(arr[i])
    print(count)