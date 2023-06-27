import sys

r, c = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(r)]

if r%2:
    print("R"*(c-1) + ("D"+"L"*(c-1)+"D"+"R"*(c-1))*(r//2))
elif c%2:
    print("D"*(r-1) + ("R"+"U"*(r-1)+"R"+"D"*(r-1))*(c//2))
else:
    arr[0][0] = arr[r-1][c-1] = 1000
    # 뺄 칸 찾기
    min_val = 1000
    x, y = 0, 0
    for i in range(r):
        for j in range(c):
            if (i+j)%2 and arr[i][j] < min_val:
                min_val = arr[i][j]
                x, y = i, j
    # 움직이기(2줄씩 움직이기)
    # 뺄 거 나오기 전까진 우좌 순으로
    print(("R"*(c-1)+"D"+"L"*(c-1)+"D")*(x//2), end="")
    # 뺄 거 포함된 두 줄 움직이기
    if y == 0:
        print("RD"+"RURD"*(r//2-1), end="")
    else:
        if x%2:
            print("DRUR"*(y//2)+"RD"+"RURD"*((c-y-2)//2), end="")
        else:
            print("DR"+"URDR"*(y//2)+"RURD"*((c-y)//2), end="")
    # 뺄 거 나온 후엔 좌우 순으로
    print(("D"+"L"*(c-1)+"D"+"R"*(c-1))*(r//2-1-x//2))

