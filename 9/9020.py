from sys import stdin

nums = [True for _ in range(10001)]
nums[1] = False
for i in range(2, 101):
    if nums[i]:
        j = 2
        while j * i <= 10000:
            nums[j*i] = False
            j += 1


T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    a, b = (N//2, N//2)
    for i in range(N//2):
        if nums[a-i] and nums[a+i]:  # 더해서 N이 되는 두 수의 평균(수직선에서의 중점) = N/2 이므로 두 수는 N/2-x,N/2+x 로 표시 가능!!
            print(a-i, a+i)
            break
