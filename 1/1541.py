s = (input()+"-0").split("-", 1)
print(sum(map(int, s[0].split("+"))) - sum(map(int, s[1].replace("-", "+").split("+"))))