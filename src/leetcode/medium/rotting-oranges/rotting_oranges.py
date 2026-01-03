""" """


def getOrangesToInfect(grid: list[list[int]], y: int, x: int) -> list[list[int]]:
    oranges = []

    if y > 0 and grid[y - 1][x] == 1:
        oranges.append([y - 1, x])
    if y < len(grid) - 1 and grid[y + 1][x] == 1:
        oranges.append([y + 1, x])
    if x > 0 and grid[y][x - 1] == 1:
        oranges.append([y, x - 1])
    if x < len(grid[y]) - 1 and grid[y][x + 1] == 1:
        oranges.append([y, x + 1])

    return oranges


def orangesRotting(grid: list[list[int]]) -> int:
    rotten = {}
    minutes = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 2 and len(getOrangesToInfect(grid, y, x)) > 0:
                rotten[f"{y},{x}"] = [y, x]

    while len(rotten.keys()) > 0:
        updatedRotten = {}
        for key in rotten.keys():
            y, x = rotten[key]
            possibleInfections = getOrangesToInfect(grid, y, x)

            for infection in possibleInfections:
                grid[infection[0]][infection[1]] = 2
                if len(getOrangesToInfect(grid, infection[0], infection[1])) > 0:
                    updatedRotten[f"{infection[0]},{infection[0]}"] = [
                        infection[0],
                        infection[1],
                    ]

        rotten = updatedRotten
        minutes += 1

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 1:
                return -1

    return minutes
