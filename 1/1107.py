n = int(input())
m = int(input())
if m != 0:
    broken = set(input())
else:
    broken = set()
button = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'} - broken
x = abs(n - 100)  # 시작 채널인 100번에서 목표 채널까지 +-만을 눌러서 움직일 때 눌러야 하는 횟수

if n == 100:  # 시작 = 목표이므로 안눌러도 됨
    print(0)
elif m == 10:  # 모든 버튼이 고장났으므로 아래 확인 할 필요 x
    print(x)
else:
    a, b = 1000000, 1000000  # x보다 큰 적당한 수(탐색 실패할 경우 min함수에서 걸러지게)
    for i in range(x+1):  # i = x 일 때 a = len(str(n+i)) + x > x 이므로 x까지만 검색
        to_c = str(n + i)  # 버튼을 눌러서 갈 채널
        if not set(to_c) - button:
            a = len(str(n + i)) + i
            break
    for i in range(1, n+1):  # i = n 일때 to_c = 0으로 최솟값. 음수 채널로는 갈 수 없으므로 n까지만 검색
        to_c = str(n - i)
        if not set(to_c) - button:
            b = len(str(n - i)) + i
            break
    print(min(a, b, x))
