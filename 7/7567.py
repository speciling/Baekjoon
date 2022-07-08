s = input()
before = 0
h = 0
for i in s:
    if i == before:
        h += 5
    else:
        h += 10
        before = i
print(h)
