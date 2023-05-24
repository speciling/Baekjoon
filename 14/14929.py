n = int(input())
arr = list(map(int, input().split()))
suffixsum = [0] * (n - 1) + [arr[-1]]
for i in range(n-2, 0, -1):
    suffixsum[i] = suffixsum[i + 1] + arr[i]
print(sum(arr[i] * suffixsum[i + 1] for i in range(n - 1)))