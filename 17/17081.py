import sys
input = sys.stdin.readline

n, m = map(int, input().split())
greed = [list(input().strip()) for _ in range(n)]
movement = input().strip()
monster_num = 0
for i in range(n):
    monster_num += greed[i].count('&')
monsters = [list(input().strip()) for _ in range(monster_num + 1)]
boxes_num = 0
for i in range(n):
    boxes_num += greed[i].count('B')
boxes = [list(input().strip()) for _ in range(boxes_num)]

player = {
    'LV': 1,
    'HP': [20, 20],
    'ATT': [2, 0],
    'DEF': [2, 0],
    'EXP': [0, 5]
}

for i in range(n):
    try:
        player_location = [i, greed[i].index('@')]
        greed[i][player_location[1]] = '.'
        break
    except:
        continue

def level_up():
    player['LV'] += 1
    player['HP'][1] += 5
    player['HP'][0] = player['HP'][1]
    player['ATT'][0] += 2
    player['DEF'][0] += 2
    player['EXP'][0] = 0
    player['EXP'][1] += 5


def move(direction):
    to_move = []
    global player_location
    if direction == 'R':
        try:
            to_move = [player_location[0],player_location[1]+1]
        except IndexError:
            to_move = player_location
    elif direction == 'L':
        try:
            to_move = [player_location[0],player_location[1]-1]
        except IndexError:
            to_move = player_location
    elif direction == 'U':
        try:
            to_move = [player_location[0]-1,player_location[1]]
        except IndexError:
            to_move = player_location
    else:
        try:
            to_move = [player_location[0]+1,player_location[1]-1]
        except IndexError:
            to_move = player_location

    if greed[to_move[0]][to_move[1]] == '.':
        player_location = to_move
    elif greed[to_move[0]][to_move[1]] == '#':
        to_move = player_location






for _ in range(len(movement)):
