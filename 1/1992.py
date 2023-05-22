n = int(input())
img = [input() for _ in range(n)]


def quadtree(row, col, size):
    dot = img[row][col]
    if size == 1:
        return dot
    for i in range(row, row+size):
        for j in range(col, col+size):
            if img[i][j] != dot:
                nSize = size//2
                return "(" + quadtree(row, col, nSize) + quadtree(row, col + nSize, nSize) \
                       + quadtree(row + nSize, col, nSize) + quadtree(row + nSize, col + nSize, nSize) + ")"
    return dot


print(quadtree(0, 0, n))

