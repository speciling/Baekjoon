from sys import stdin
input = stdin.readline

paper = [list(input().split()) for _ in range(int(input()))]
around = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
cnt = [0, 0, 0]

while len(paper) >= 3:
    attached = [[False]*(len(paper)//3) for _ in range(len(paper)//3)]
    for i in range(0, len(paper), 3):
        for j in range(0, len(paper), 3):
            arounds = [paper[i+dx][j+dy] for dx,dy in around]
            # 주변 4개 조각이 모두 같으면 한 조각으로 붙인다
            if all(arounds[0] == arounds[idx] for idx in range(1,9)):
                attached[i//3][j//3] = arounds[0]
            # 같지 않으면 각 조각의 수를 센다
            else:
                for color in arounds:
                    if color:
                        cnt[int(color)+1] += 1
    paper = attached

if paper[0][0]:
    cnt[int(paper[0][0])+1] += 1

print('\n'.join(map(str, cnt)))