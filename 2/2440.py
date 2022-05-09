def star(n: int):
    print('*'*n)
    if n > 1:
        star(n-1)


star(int(input()))
