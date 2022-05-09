N = int(input())
ans = 0

if N <= 18:
    n = 0
else:
    n = N - len(str(N)) * 9  # 자리수의 합의 최댓값을 빼 준 숫자부터 for문을 돌려서 처리시간이 빨라지도록 함.

for i in range(n, N):
    d_sum = i
    for j in range(len(str(i))):
        d_sum += int(str(i)[j])
    if d_sum == N:
        ans = i
        break

print(ans)
