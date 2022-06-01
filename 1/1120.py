a, b = input().split()
differences = []
for i in range(len(b)-len(a)+1):
    count = 0
    for j in range(len(a)):
        if a[j] != b[j+i]:
            count += 1
    differences.append(count)
print(min(differences))
