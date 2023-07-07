print("\n".join(sorted(set(open(0).read().split()[1:]), key=lambda x: (len(x), x))))

# words = set(open(0).read().split()[1:])
# words = sorted(words, key=lambda x: (len(x), x))
# print("\n".join(words))