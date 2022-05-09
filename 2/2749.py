"""
def find_pp(num):  # 피사노 주기 찾는 함수
    a = 0
    b = 1
    n = 1
    i = 1
    while True:
        n = (a + b)%num
        a = b
        b = n
        i += 1
        if n == 0:
            n = (a + b)%num
            a = b
            b = n
            i += 1
            if n == 1:
                break
    print(i-1)
"""

n = int(input()) % 1500000

if n < 2:
    print(n)
else:
    a, b = 0, 1
    total = 0
    for i in range(2, n+1):
        total = (a + b) % 1000000
        a = b
        b = total
    print(b)