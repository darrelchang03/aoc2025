from collections import deque
import copy


def day4():

    with open('day4_input.txt', 'r') as f:
        grid = [line.rstrip() for line in f]
        cleanGrid = []
        for line in grid:
            cleanLine = [] 
            for c in line:
                cleanLine.append(c)
            cleanGrid.append(cleanLine)
        grid = cleanGrid

        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [
            (0, 1), # RIGHT
            (0, -1),# LEFT
            (1, 0), # UP
            (-1, 0),# DOWN
            (-1, 1), # UP RIGHT
            (-1, -1), # UP LEFT
            (1, 1), # DOWN RIGHT
            (1, -1), # DOWN LEFT
        ]
        res = 0
        papersRemoved = 1
        while papersRemoved:
            papersRemoved = 0
            coordsRemoved = []
            for i in range(ROWS):
                for j in range(COLS):
                    numAdjacent = 0
                    if i >= ROWS or i < 0 or j >= COLS or j < 0:
                        continue
                    if grid[i][j] == '.':
                        continue
                    for dy, dx in dirs:
                        ny = i + dy 
                        nx = j + dx
                        if ny >= ROWS or ny < 0 or nx >= COLS or nx < 0:
                            continue
                        if grid[ny][nx] == '@':
                            numAdjacent += 1
                    if numAdjacent < 4:
                        coordsRemoved.append((i, j))
                        papersRemoved += 1
            for i, j in coordsRemoved:
                grid[i][j] = '.'
            res += papersRemoved
        return res
print(day4())
