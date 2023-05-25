def permutation(repeat, iterable):
    used = [0]*len(iterable)

    def make(seq):
        if len(seq) == repeat:
            print(*seq)
            return
        for i, num in enumerate(iterable):
            if not used[i]:
                seq.append(num)
                used[i] = 1
                make(seq)
                seq.pop()
                used[i] = 0

    make([])

permutation(int(input().split()[1]), sorted(map(int, input().split())))