from sys import stdin
input = stdin.readline

paper = [list(input().split()) for _ in range(int(input()))]
around = [[0,0], [0,1], [1,0], [1,1]]
cnt = [0, 0]

while len(paper) >= 2:
    attached = [[False]*(len(paper)//2) for _ in range(len(paper)//2)]
    for i in range(0, len(paper), 2):
        for j in range(0, len(paper), 2):
            arounds = [paper[i+dx][j+dy] for dx,dy in around]
            # 주변 4개 조각이 모두 같으면 한 조각으로 붙인다
            if all(arounds[0] == arounds[idx] for idx in range(1,4)):
                attached[i//2][j//2] = arounds[0]
            # 같지 않으면 각 조각의 수를 센다
            else:
                for color in arounds:
                    if color:
                        cnt[int(color)] += 1
    paper = attached

if paper[0][0]:
    cnt[int(paper[0][0])] += 1

print('\n'.join(map(str, cnt)))