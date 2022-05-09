from sys import stdin

n, m = [int(stdin.readline()) for _ in range(2)]
if m != 0:
        broken = set(stdin.readline())
else:
    broken = set()
button = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'} - broken

a, b = 1000000, 1000000

for i in range(500000):
    to_c = str(n + i)
    if not set(to_c) - button:
        a = len(str(n + i)) + i
        break

for i in range(500000):
    to_c = str(n - i)
    if not set(to_c) - button:
        b = len(str(n - i)) + i
        break


if n == 100:
    print(0)

elif m == 10:
    print(n-100 if n >= 100 else 100-n)

else:
    if n > 100:
        x = n-100
    else:
        x = 100-n
    if x < a and x < b:
        print(n-100)
    else:
        print(a if a <= b else b)
