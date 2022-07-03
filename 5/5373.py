from sys import stdin


def spin(direction):
    if direction == 'U+':
        turn_r('U')
        seq = ('F', 'L', 'B', 'R')
        ud_spin(direction, seq)
    if direction == 'U-':
        turn_l('U')
        seq = ('F', 'R', 'B', 'L')
        ud_spin(direction, seq)
    if direction == 'D+':
        turn_r('D')
        seq = ('F', 'R', 'B', 'L')
        ud_spin(direction, seq)
    if direction == 'D-':
        seq = ('F', 'L', 'B', 'R')
        turn_l('D')
        ud_spin(direction, seq)
    if direction == 'F+':
        turn_r('F')
        seq = ('U', 'R', 'D', 'L')
        fb_spin(direction, seq)
    if direction == 'F-':
        turn_l('F')
        seq = ('U', 'L', 'D', 'R')
        fb_spin(direction, seq)
    if direction == 'B+':
        turn_r('B')
        seq = ('U', 'L', 'D', 'R')
        fb_spin(direction, seq)
    if direction == 'B-':
        turn_l('B')
        seq = ('U', 'R', 'D', 'L')
        fb_spin(direction, seq)
    if direction == 'L+':
        turn_r('L')
        seq = ('U', 'F', 'D', 'B')
        lr_spin(direction, seq)
    if direction == 'L-':
        turn_l('L')
        seq = ('U', 'B', 'D', 'F')
        lr_spin(direction, seq)
    if direction == 'R+':
        turn_r('R')
        seq = ('U', 'B', 'D', 'F')
        lr_spin(direction, seq)
    if direction == 'R-':
        turn_l('R')
        seq = ('U', 'F', 'D', 'B')
        lr_spin(direction, seq)


def turn_r(side):
    temp = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            temp[i][j] = cube[side][2-j][i]
    cube[side] = temp


def turn_l(side):
    temp = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            temp[i][j] = cube[side][j][2-i]
    cube[side] = temp


def ud_spin(direction, seq):
    x = 0 if direction[0] == 'U' else 2
    cube[seq[0]][x], cube[seq[1]][x], cube[seq[2]][x], cube[seq[3]][x] = cube[seq[3]][x], cube[seq[0]][x], cube[seq[1]][x], cube[seq[2]][x]


def fb_spin(direction, seq):
    x = 0 if direction[0] == 'F' else 2
    if direction == 'F+' or direction == 'B-':
        temp = cube[seq[0]][2-x]
        temp2 = []
        for i in range(3):
            temp2.append(cube[seq[1]][i][x])
            cube[seq[1]][i][x] = temp[i]
        temp = cube[seq[2]][x]
        temp2.reverse()
        cube[seq[2]][x] = temp2
        temp2 = []
        for i in range(3):
            temp2.append(cube[seq[3]][i][2-x])
            cube[seq[3]][i][2-x] = temp[i]
        temp2.reverse()
        cube[seq[0]][2-x] = temp2
    else:
        temp = cube[seq[0]][2-x]
        temp2 = []
        temp.reverse()
        for i in range(3):
            temp2.append(cube[seq[1]][i][2-x])
            cube[seq[1]][i][2-x] = temp[i]
        temp = cube[seq[2]][x]
        cube[seq[2]][x] = temp2
        temp2 = []
        temp.reverse()
        for i in range(3):
            temp2.append(cube[seq[3]][i][x])
            cube[seq[3]][i][x] = temp[i]
        cube[seq[0]][2-x] = temp2


def lr_spin(direction, seq):
    x = 0 if direction[0] == 'L' else 2
    temp = []
    temp2 = []
    if direction == 'L+' or direction == 'R-':
        for i in range(3):
            temp.append(cube[seq[0]][i][x])
        for i in range(1, 3):
            for j in range(3):
                temp2.append(cube[seq[i]][j][x])
                cube[seq[i]][j][x] = temp[j]
            temp = temp2
            temp2 = []
        for i in range(3):
            temp2.append(cube[seq[3]][i][2-x])
            cube[seq[3]][i][2-x] = temp[2-i]
        for i in range(3):
            cube[seq[0]][i][x] = temp2[2-i]
    else:
        for i in range(3):
            temp.append(cube[seq[0]][i][x])
        for i in range(3):
            temp2.append(cube[seq[1]][i][2-x])
            cube[seq[1]][i][2-x] = temp[2-i]
        temp2.reverse()
        temp = temp2
        temp2 = []
        for i in range(2, 4):
            for j in range(3):
                temp2.append(cube[seq[i]][j][x])
                cube[seq[i]][j][x] = temp[j]
            temp = temp2
            temp2 = []
        for i in range(3):
            cube[seq[0]][i][x] = temp[i]


for _ in range(int(input())):
    stdin.readline()
    cube = {'U': [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']],  # 위(U)
            'D': [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']],  # 아래(D)
            'F': [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],  # 앞(F)
            'B': [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']],  # 뒤(B)
            'L': [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],  # 좌(L)
            'R': [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]}  # 우(R)
    for d in stdin.readline().strip().split():
        spin(d)
    for i in range(3):
        print(''.join(cube['U'][i]))