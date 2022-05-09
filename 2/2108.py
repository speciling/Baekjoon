from sys import stdin

n = int(stdin.readline())

nums = [int(stdin.readline()) for _ in range(n)]
nums.sort()
counts = [0] * 8001
total = 0

for i in nums:
    counts[i+4000] += 1  # count[n] = n-4000의 개수
    total += i

mode = [[0, 0]]  # 최빈값 [[숫자,개수]] 형태
for i in range(8001):
    if counts[i] > mode[0][1]:  # i의 개수를 확인해서 최빈값에 저장 된 수의 개수보다 높으면 최빈값 변겅
        mode = [[i-4000, counts[i]]]
    elif counts[i] == mode[0][1]:  # i의 개수를 확인해서 최빈값에 저장 된 수의 개수와 같으면 최빈값 추가
        mode.append([i-4000, counts[i]])

if len(mode) >= 2:  # 최빈값이 2개 이상이면 2번째 최빈값을 저장
    mode_num = mode[1][0]
else:
    mode_num = mode[0][0]

print(f'{round(total/n)}\n{nums[int((n+1)/2)-1]}\n{mode_num}\n{nums[-1]-nums[0]}')