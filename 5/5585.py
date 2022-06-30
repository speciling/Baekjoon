change = 1000 - int(input())
print(change//500 + (change%500)//100 + (change%100)//50 + (change%50)//10 + (change%10)//5 + change%5)