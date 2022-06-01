m, d = map(int, input().split())
day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

days = sum(month_days[:m-1]) + d
print(day[(days-1) % 7])