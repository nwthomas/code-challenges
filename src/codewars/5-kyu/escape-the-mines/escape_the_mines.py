"""
https://www.codewars.com/kata/5326ef17b7320ee2e00001df/python

A poor miner is trapped in a mine and you have to help him to get out !

Only, the mine is all dark so you have to tell him where to go.

In this kata, you will have to implement a method solve(map, miner, exit) that has to return the path the miner must take to reach the exit as an array of moves, such as : ['up', 'down', 'right', 'left']. There are 4 possible moves, up, down, left and right, no diagonal.

map is a 2-dimensional array of boolean values, representing squares. false for walls, true for open squares (where the miner can walk). It will never be larger than 5 x 5. It is laid out as an array of columns. All columns will always be the same size, though not necessarily the same size as rows (in other words, maps can be rectangular). The map will never contain any loop, so there will always be only one possible path. The map may contain dead-ends though.

miner is the position of the miner at the start, as an object made of two zero-based integer properties, x and y. For example {x:0, y:0} would be the top-left corner.

exit is the position of the exit, in the same format as miner.

Note that the miner can't go outside the map, as it is a tunnel.

Let's take a pretty basic example:

map = [[True, False],
    [True, True]];

solve(map, {'x':0,'y':0}, {'x':1,'y':1})

Should return ['right', 'down']
"""


def find_mine_escape_path(map, miner, exit):
    if len(map) <= 0:
        return []

    visited_set = set()
    visited_set.add((miner["x"], miner["y"]))

    def move(x, y, visited, path=[]):
        if x == exit["x"] and y == exit["y"]:
            return path
        if x + 1 < len(map) and map[x + 1][y] and (x + 1, y) not in visited:
            visited.add((x + 1, y))
            return move(x + 1, y, visited, path + ["right"])
        if y + 1 < len(map[x]) and map[x][y + 1] and (x, y + 1) not in visited:
            visited.add((x, y + 1))
            return move(x, y + 1, visited, path + ["down"])
        if x - 1 >= 0 and map[x - 1][y] and (x - 1, y) not in visited:
            visited.add((x - 1, y))
            return move(x - 1, y, visited, path + ["left"])
        if y - 1 >= 0 and map[x][y - 1] and (x, y - 1) not in visited:
            visited.add((x, y - 1))
            return move(x, y - 1, visited, path + ["up"])

    return move(miner["x"], miner["y"], visited_set)
