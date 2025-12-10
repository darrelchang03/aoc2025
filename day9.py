from collections import deque

def getPoints(fileName):
    with open(fileName, 'r') as f:
        reds = [tuple(int(x) for x in line.strip().split(',')) for line in f.readlines()]
    greens = []
    reds.append((reds[0]))
    for i, redPoint in enumerate(reds[:-1]):
        x, y = redPoint
        nextX, nextY = reds[i+1]
        if y == nextY:
            smallerX, biggerX = min(x, nextX), max(x, nextX)
            for x in range(smallerX + 1, biggerX):
                greens.append((x, y))
        elif x == nextX:
            smallerY, biggerY = min(y, nextY), max(y, nextY)
            for y in range(smallerY + 1, biggerY):
                greens.append((x, y))
    return reds[:-1], greens

def getPointsInRectangle(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    smallerX, biggerX = min(x1, x2), max(x1, x2)
    smallerY, biggerY = min(y1, y2), max(y1, y2)
    return [ (x, y) for y in range(smallerY, biggerY + 1) for x in range(smallerX, biggerX+1)]

def getInteriorPoints(reds, greens):
    xs = [x for x, _ in reds]
    ys = [y for _, y in reds]
    
    # Padding around
    minX = min(xs) - 1
    minY = min(ys) - 1
    maxX = max(xs) + 1
    maxY = max(ys) + 1

    start = None
    reds, greens = set(reds), set(greens)
    blocked = reds | greens
    for x in range(minX, maxX + 1):
        if (x, minY) not in blocked:
            start = (x, minY)
            break
        if (x, maxY) not in blocked:
            start = (x, maxY)
            break
    if start is None:
        for y in range(minY, maxY + 1):
            if (minX, y) not in blocked:
                start = (minX, y)
                break
            if (maxX, y) not in blocked:
                start = (maxX, y)
                break
    if start is None:
        raise(ValueError("Input is not correct"))

    exterior = set([start])
    q = deque([start])

    minX_local, maxX_local = minX, maxX
    minY_local, maxY_local = minY, maxY
    blocked_local = blocked
    exterior_local = exterior

    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if (nx < minX_local or nx > maxX_local or
                ny < minY_local or ny > maxY_local):
                continue
            if (nx, ny) in exterior_local or (nx, ny) in blocked_local:
                continue
            p = (nx, ny)
            exterior_local.add(p)
            q.append(p)

    # all points in bounding box that are not exterior and not blocked
    interior_points = {
        (x, y)
        for x in range(minX, maxX + 1)
            for y in range(minY, maxY + 1)
        if (x, y) not in exterior_local and (x, y) not in blocked_local
    }

    return interior_points

def part1(points):
    maxArea = 0
    for i, (x1, y1) in enumerate(points):
        for x2, y2 in points[i+1:]:
            maxArea = max(maxArea, ((abs(y1 - y2) + 1) * (abs(x1 - x2) + 1)))
    return maxArea

def part2(redTiles, greenTiles, interiorTiles):
    maxArea = 0
    validTiles = set(redTiles) | set(greenTiles) | set(interiorTiles)
    for i, (x1, y1) in enumerate(redTiles):
        for x2, y2 in redTiles[i+1:]:
            area = ((abs(y1 - y2) + 1) * (abs(x1 - x2) + 1))
            #print(area)
            if area > maxArea:
                # if a single point in rectangle is not in interior
                for rectanglePoint in getPointsInRectangle((x1, y1), (x2, y2)):
                    if rectanglePoint not in validTiles:
                        break
                else:
                    maxArea = area
    return maxArea

redTiles, greenTiles = getPoints('day9_input.txt')
interiorTiles = getInteriorPoints(redTiles, greenTiles)

part1Res = part1(list(redTiles))
part2Res = part2(redTiles, greenTiles, interiorTiles)
print(part2Res)


