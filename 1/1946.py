from sys import stdin

for _ in range(int(stdin.readline())):  # 테스트 케이스 반복
    n = int(stdin.readline())
    ranking = sorted([list(map(int, stdin.readline().split())) for _ in range(n)])
    x = n+1  # x에는 for문 돌면서 면접(두 번째) 순위중에 가장 작은 값 저장
    cnt = 0
    for i in ranking:
        if i[1] < x:  # i[1] > x 이다 == i보다 서류 순위가 낮은 사람중에 면접 순위도 낮은 사람이 있다 == 불합격
            cnt += 1
            x = i[1]
    print(cnt)
