from sys import stdin

for s in stdin:
    lower, upper, digit, space = 0, 0, 0, 0
    for a in s.rstrip('\n'):
        if a.islower():
            lower += 1
        elif a.isupper():
            upper += 1
        elif a.isdigit():
            digit += 1
        else:
            space += 1
    print(lower, upper, digit, space)