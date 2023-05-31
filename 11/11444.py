def matrixmul(matrix1, matrix2):
    r, c, n = len(matrix1), len(matrix2[0]), len(matrix2)
    res = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            tmp = 0
            for k in range(n):
                tmp += matrix1[i][k] * matrix2[k][j]
            res[i][j] = tmp%1000000007
    return res


def fibo(n):
    arr = ((1, 1), (1, 0))
    res = ((1, 1), (1, 0))
    operate = []
    while n > 1:
        if n % 2:
            n -= 1
            operate.append(1)
        else:
            n //= 2
            operate.append(0)
    while operate:
        if operate.pop():
            res = matrixmul(res, arr)
        else:
            res = matrixmul(res, res)

    return res[0][1]


print(fibo(int(input())))