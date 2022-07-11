from sys import stdin
n, k = map(int, input().split())
stuff = [[0, 0]] + [list(map(int, stdin.readline().split())) for _ in range(n)]
stuff.sort()
dp = [0] * (k+1)  # 최대 무게가 k일때 가치의 최댓값 = dp[k]
for w, v in stuff:  # 가벼운 순서대로 물건 꺼낸다
    for i in range(k, -1, -1):
        if w > i:  # 물건의 무게가 최대무게보다 무거워지면 중지
            break
        dp[i] = max(dp[i], dp[i-w] + v)
        # dp[i]가 큰 경우 : 다른 물건을 빼서 넣는것보다 현재 물건을 넣지 않을때가 가치가 높음
        # dp[i-w]+v 가 큰 경우 : 무게가 남아서(dp[i] == dp[i-w]) 총 가치 커짐 or 다른 물건을 빼서 넣으면 가치가 높아짐
print(dp[k])
