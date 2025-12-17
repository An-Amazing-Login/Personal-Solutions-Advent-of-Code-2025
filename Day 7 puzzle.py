"""first half: Tachyon splitting in the laboratories"""

with open("input puzzle 7", "r", encoding="utf-8") as inputFile:
    autoInput = list(inputFile)
manualInput = [
    ".......S.......\n",
    "...............\n",
    ".......^.......\n",
    "...............\n",
    "......^.^......\n",
    "...............\n",
    ".....^.^.^.....\n",
    "...............\n",
    "....^.^...^....\n",
    "...............\n",
    "...^.^...^.^...\n",
    "...............\n",
    "..^...^.....^..\n",
    "...............\n",
    ".^.^.^.^.^...^.\n",
    "...............\n",
]
# print(manualInput)

rawInput = [string[:-1] for string in autoInput]
# print(rawInput)


def splitCounter(grid):
    """Counts the amount of times the beam is split, by drawing the full 'classical' diagram."""
    counter = 0
    mutableGrid = []
    for word in grid:
        line = []
        for character in word:
            line.append(character)
        mutableGrid.append(line)
    # print(mutableGrid)

    for i in range(len(grid[:-1])):
        for j in range(len(grid[i])):
            if mutableGrid[i][j] == "S":
                mutableGrid[i + 1][j] = "|"
            elif (mutableGrid[i][j] == "|") and (grid[i + 1][j] == "^"):
                mutableGrid[i + 1][j - 1] = "|"
                mutableGrid[i + 1][j + 1] = "|"
                counter += 1
            elif mutableGrid[i][j] == "|":
                mutableGrid[i + 1][j] = "|"
            else:
                continue
    return counter


print(splitCounter(rawInput))

"""second half: quantum tachyon manifold"""


def classicalDiagramMaker(grid):
    """Returns a 'classical' diagram with all splits drawn."""
    mutableGrid = []
    for word in grid:
        line = []
        for character in word:
            line.append(character)
        mutableGrid.append(line)
    for i in range(len(grid[:-1])):
        for j in range(len(grid[i])):
            if mutableGrid[i][j] == "S":
                mutableGrid[i + 1][j] = "|"
            elif (mutableGrid[i][j] == "|") and (grid[i + 1][j] == "^"):
                mutableGrid[i + 1][j - 1] = "|"
                mutableGrid[i + 1][j + 1] = "|"
            elif mutableGrid[i][j] == "|":
                mutableGrid[i + 1][j] = "|"
            else:
                continue
    return mutableGrid


dia1 = classicalDiagramMaker(rawInput)


def quantumDiagramMaker(grid):
    """Returns a grid that counts all paths from the bottom up.
    Needs a 'classical' diagram with all splits drawn."""
    mutableGrid = grid  # shallow copy
    height = len(grid)
    for j, char in enumerate(grid[-1]):
        if char == "|":
            mutableGrid[-1][j] = 1

    for i in range(height - 2, -1, -1):
        for j in range(len(grid[i])):
            if (grid[i][j] == "|") and (grid[i + 1][j] == "^"):
                mutableGrid[i][j] = (
                    mutableGrid[i + 1][j - 1] + mutableGrid[i + 1][j + 1]
                )
            elif (grid[i][j] == "|") or (grid[i][j] == "S"):
                mutableGrid[i][j] = mutableGrid[i + 1][j]
            else:
                continue

    return mutableGrid


startPoint = rawInput[0].index("S")
# print(quantumDiagramMaker(dia1)) #this is pretty! but needs extended output.
print(quantumDiagramMaker(dia1)[0][startPoint])
