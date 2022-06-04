n = int(input())
dice = list(map(int, input().split()))
if n == 1:
    print(sum(dice) - max(dice))
else:
    sum_2 = []
    sum_3 = []
    for i in range(4):
        sum_2.append(dice[0] + dice[1+i])
        sum_2.append(dice[-1] + dice[1+i])
    for i in range(2):
        sum_2.append(dice[1] + dice[2+i])
        sum_3.append(dice[1] + dice[2+i])
        sum_2.append(dice[4] + dice[2+i])
        sum_3.append(dice[4] + dice[2 + i])
    minimum_sum_2 = min(sum_2)
    minimum_sum_3 = min(sum_3) + min(dice[0], dice[-1])
    print(4*minimum_sum_3 + (8*n-12)*minimum_sum_2 + (5*n*n-16*n+12)*min(dice))
