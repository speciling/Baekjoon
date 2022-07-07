w = input()
for i in range(len(w)//2):
    if w[i] != w[-i-1]:
        print(0)
        break
else:
    print(1)