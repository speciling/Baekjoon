n, m, k = map(int, input().split())
teams = min(n//2, m)
k -= n+m-3*teams
print(teams if k <= 0 else teams-(k//3+(k%3!=0)))