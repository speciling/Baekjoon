from sys import stdin

n, k = map(int, stdin.readline().split())
d = {i: [0, 0] for i in range(1, 7)}
students = [map(int, stdin.readline().split()) for _ in range(n)]
for sex, grade in students:
    d[grade][sex] += 1
room = 0
for grade in range(1, 7):
    for sex in range(2):
        room += d[grade][sex] // k
        if d[grade][sex] % k:
            room += 1
print(room)