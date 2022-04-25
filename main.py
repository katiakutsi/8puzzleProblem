from __future__ import print_function
import sys

def misplacedTiles(currentState):
    numberOfMisplacedTiles = 0
    goal = [1, 2, 3,
            4, 5, 6,
            7, 8, 0]

    for i in range(len(goal)):
        if currentState[i] != 0 and currentState[i] != goal[i]:
            numberOfMisplacedTiles += 1

    return numberOfMisplacedTiles

def printAsMatrix(list):
    for i in range(len(list)):
        if i % 3 == 0 and i > 0:
            print("")
        print(str(list[i]) + " ", end="")

def move(indexes, position, state):
    minMisplacedTilesNumber = sys.maxint
    storedState = list(state)

    for i in range(len(indexes)):
        duplicatedState = list(state)

        duplicatedState[position] = duplicatedState[indexes[i]]
        duplicatedState[indexes[i]] = 0

        misplacedTilesNumber = misplacedTiles(duplicatedState)

        if misplacedTilesNumber < minMisplacedTilesNumber:
            minMisplacedTilesNumber = misplacedTilesNumber
            storedState = list(duplicatedState)

    return storedState, minMisplacedTilesNumber

if __name__ == '__main__':

    state = []

    while len(state) != 9:
        x = input("Enter " + str(len(state)) + " element : ")
        state.append(x)

    heuristicValue = misplacedTiles(state)
    level = 1

    print("\n--- Level --- " + str(level))
    printAsMatrix(state)
    print("\nHeuristic Value : " + str(heuristicValue))

    while heuristicValue > 0:
        position = state.index(0)
        level += 1
        possibleIndexesOfEmptyTile = []

        if position == 0:
            possibleIndexesOfEmptyTile = [1, 3]
        elif position == 1:
            possibleIndexesOfEmptyTile = [0, 2, 4]
        elif position == 2:
            possibleIndexesOfEmptyTile = [1, 5]
        elif position == 3:
            possibleIndexesOfEmptyTile = [0, 4, 6]
        elif position == 4:
            possibleIndexesOfEmptyTile = [1, 3, 5, 7]
        elif position == 5:
            possibleIndexesOfEmptyTile = [2, 4, 8]
        elif position == 6:
            possibleIndexesOfEmptyTile = [3, 7]
        elif position == 7:
            possibleIndexesOfEmptyTile = [4, 6, 8]
        elif position == 8:
            possibleIndexesOfEmptyTile = [5, 6]

        state, heuristicValue = move(possibleIndexesOfEmptyTile, position, state)

        print("\n-- Level -- " + str(level))
        printAsMatrix(state)
        print("\nHeuristic Value : " + str(heuristicValue))