for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    if s1 > s2:
        m2 -= 1
        s2 += 60
    if m1 > m2:
        h2 -= 1
        m2 += 60
    print(h2-h1, m2-m1, s2-s1)