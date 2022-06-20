n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
sums = []
for i in range(n):
    for j in range(m):
        #paper[i][j]
        if j + 3 < m:
            sums.append(paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i][j+3])  # 1_1 ㅡ
        if i + 3 < n:
            sums.append(paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+3][j])  # 1_2 ㅣ
        if i + 1 < n and j + 1 < m:
            sums.append(paper[i][j] + paper[i][j+1] + paper[i+1][j] + paper[i+1][j+1])  # 2 ㅁ
        if i + 2 < n and j + 1 < m:
            sums.append(paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+2][j+1])  # 3_1 L
            sums.append(paper[i][j] + paper[i][j + 1] + paper[i + 1][j] + paper[i + 2][j])  # 3_5 좌우반전 ㄱ
            sums.append(paper[i][j] + paper[i][j + 1] + paper[i + 1][j + 1] + paper[i + 2][j + 1])  # 3_6 ㄱ
            sums.append(paper[i][j] + paper[i + 1][j] + paper[i + 1][j + 1] + paper[i + 2][j + 1])  # 4_1 기본
            sums.append(paper[i][j] + paper[i + 1][j] + paper[i + 1][j + 1] + paper[i + 2][j])  # 5_4 ㅏ
        if i + 2 < n and j > 0:
            sums.append(paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+2][j-1])  # 3_2 좌우반전 L
            sums.append(paper[i][j] + paper[i + 1][j] + paper[i + 1][j - 1] + paper[i + 2][j - 1])  # 4_2 좌우반전
            sums.append(paper[i][j] + paper[i+1][j] + paper[i + 1][j - 1] + paper[i + 2][j])  # 5_2 ㅓ
        if i + 1 < n and j + 2 < m:  # 3_3,4
            sums.append(paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j+2])  # 3_3 ¬
            sums.append(paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j])  # 3_7 좌우반전 ¬
            sums.append(paper[i][j] + paper[i][j + 1] + paper[i+1][j + 1] + paper[i + 1][j+2])  # 4_3 y=x 대칭
            sums.append(paper[i][j] + paper[i][j + 1] + paper[i + 1][j + 1] + paper[i][j + 2])  # 5_1 ㅜ
        if i > 0 and j + 2 < m:
            sums.append(paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + paper[i - 1][j + 2])  # 3_4 ⨼
            sums.append(paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + paper[i - 1][j])  # 3_8 ⨽
            sums.append(paper[i][j] + paper[i][j + 1] + paper[i - 1][j + 1] + paper[i - 1][j + 2])  # 4_4 오른쪽으로 돌리기
            sums.append(paper[i][j] + paper[i][j + 1] + paper[i - 1][j + 1] + paper[i][j + 2])  # 5_3 ㅗ

print(max(sums))