n = int(input())
h = list(map(int, input().split()))

i = 0
j = 1
k = 0
kills = []
while True:
    if h[i] <= h[j]:
        kills.append(k)
        k = 0
        i = j
        j += 1
    else:
        j += 1
        k += 1
    if j == n:
        kills.append(k)
        break

print(max(kills))