# n번까지의 원판을 1번에서 3번으로 옮긴다
# -> n-1번 1에서 2 , n번 1에서 3, n-1번 2에서 3
# -> n-2번 1에서 3, n-1번 1에서 2, n-2번 3에서 1, n번 1에서 3, n-2번 2에서 1, n-1번 2에서 3, n-2번 1에서 3
# ...

# 일반화
# n번까지의 원판을 a번에서 b번으로 옮긴다
# -> n-1번 a에서 c , n번 a에서 b, n-1번 c에서 b
# -> n-2번 a에서 b, n-1번 a에서 c, n-2번 b에서 c, n번 a에서 b, n-2번 c에서 a, n-1번 c에서 b, n-2번 a에서 b

# 메모이제이션 사용
# (n, a, b)를 key값으로 갖고 move(n, a, b)의 출력값을 value값으로 갖는 cache 딕셔너리 생성
# n, a, b값이 동일할 때 move(n, a, b)를 두 번 이상 실행하지 않고 cache에서 그 결과값을 가져옴으로써 시간 단축

def move(n, a, b):  # n번까지의 원판을 a기둥에서 b기둥으로 이동
    if n == 1:
        return f'{a} {b}\n'
    if (n, a, b) in cache:
        return cache[(n, a, b)]
    c = 6 - (a + b)  # a, b 가 아닌 다른 기둥
    cache[(n, a, b)] = f'{move(n-1, a, c)}{a} {b}\n{move(n-1, c, b)}'
    return cache[(n, a, b)]


cache = {}
n = int(input())
print(2**n - 1)
print(move(n, 1, 3))
