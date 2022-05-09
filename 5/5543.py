gets = [int(input()) for _ in range(5)]
print(min(gets[:3]) + min(gets[3:]) - 50)