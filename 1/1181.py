from sys import stdin

n = int(stdin.readline())
words = list({stdin.readline().rstrip() for _ in range(n)})
words.sort(key= lambda x : (len(x), x))

print('\n'.join(words))