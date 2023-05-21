word = input()
c_word = ''
for c in word:
    c_word += chr(ord(c)-3) if ord(c) >= 68 else chr(ord(c)+23)
print(c_word)