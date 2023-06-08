while True:
    arr = list(map(int, input().split()))
    if arr == [0, 0, 0]:
        break
    elif max(arr)*2 >= sum(arr):
        print( "Invalid" )
    else:
        arr = set(arr)
        if len(arr) == 1:
            print("Equilateral")
        elif len(arr) == 2:
            print("Isosceles")
        else:
            print("Scalene")