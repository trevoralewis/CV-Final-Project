
test_cube = [
    [[1,5,3],[5,0,5],[1,0,0]],
    [[4,4,5],[1,1,4],[2,0,1]],
    [[2,2,3],[0,2,3],[0,4,5]],
    [[4,3,0],[0,3,2],[4,5,4]],
    [[2,1,0],[3,4,2],[5,4,5]],
    [[2,3,1],[1,5,2],[3,1,3]],
]

def turnR(cube_matrix, isprime):
    if isprime == True:
        turnR(cube_matrix=cube_matrix, isprime=False)
        turnR(cube_matrix=cube_matrix, isprime=False)

    tempUC = cube_matrix[0][0][2]
    tempE = cube_matrix[0][1][2]
    tempBC = cube_matrix[0][2][2]

    cube_matrix[0][0][2] = cube_matrix[4][0][2]
    cube_matrix[0][1][2] = cube_matrix[4][1][2]
    cube_matrix[0][2][2] = cube_matrix[4][2][2]

    cube_matrix[4][0][2] = cube_matrix[5][0][2]
    cube_matrix[4][1][2] = cube_matrix[5][1][2]
    cube_matrix[4][2][2] = cube_matrix[5][2][2]

    cube_matrix[5][0][2] = cube_matrix[2][0][2]
    cube_matrix[5][1][2] = cube_matrix[2][1][2]
    cube_matrix[5][2][2] = cube_matrix[2][2][2]

    cube_matrix[2][0][2] = tempUC
    cube_matrix[2][1][2] = tempE
    cube_matrix[2][2][2] = tempBC

    temp_cube = cube_matrix
    for i in range(3):
        for j in range(3):
            cube_matrix[3][i][j] = temp_cube[3][j][2-i]

    return cube_matrix

def turnL(cube_matrix, isprime):
    if isprime == True:
        turnL(cube_matrix=cube_matrix, isprime=False)
        turnL(cube_matrix=cube_matrix, isprime=False)

    tempUC = cube_matrix[0][0][0]
    tempE = cube_matrix[0][1][0]
    tempBC = cube_matrix[0][2][0]

    cube_matrix[0][0][0] = cube_matrix[4][0][0]
    cube_matrix[0][1][0] = cube_matrix[4][1][0]
    cube_matrix[0][2][0] = cube_matrix[4][2][0]

    cube_matrix[4][0][0] = cube_matrix[5][0][0]
    cube_matrix[4][1][0] = cube_matrix[5][1][0]
    cube_matrix[4][2][0] = cube_matrix[5][2][0]

    cube_matrix[5][0][0] = cube_matrix[2][0][0]
    cube_matrix[5][1][0] = cube_matrix[2][1][0]
    cube_matrix[5][2][0] = cube_matrix[2][2][0]

    cube_matrix[2][0][0] = tempUC
    cube_matrix[2][1][0] = tempE
    cube_matrix[2][2][0] = tempBC

    temp_cube = cube_matrix
    for i in range(3):
        for j in range(3):
            cube_matrix[1][i][j] = temp_cube[1][j][2-i]

    return cube_matrix

def turnF(cube_matrix, isprime):
    tempUC = cube_matrix[3][0][0] #Save Blue
    tempE = cube_matrix[3][0][1]
    tempBC = cube_matrix[3][0][2]

    cube_matrix[1][0][0] = cube_matrix[4][0][0] #Orange to Green
    cube_matrix[1][0][1] = cube_matrix[4][0][1]
    cube_matrix[1][0][2] = cube_matrix[4][0][2]

    cube_matrix[2][0][0] = cube_matrix[1][0][0] #Green to Red
    cube_matrix[2][0][1] = cube_matrix[1][0][1]
    cube_matrix[2][0][2] = cube_matrix[1][0][2]

    cube_matrix[3][0][0] = cube_matrix[2][0][0] #Red to Blue
    cube_matrix[3][0][1] = cube_matrix[2][0][1]
    cube_matrix[3][0][2] = cube_matrix[2][0][2]

    cube_matrix[4][0][0] = tempUC #Blue to Orange
    cube_matrix[4][1][0] = tempE
    cube_matrix[4][2][0] = tempBC

    temp_cube = cube_matrix
    for i in range(3):
        for j in range(3):
            cube_matrix[0][i][j] = temp_cube[0][j][2-i]
    return cube_matrix

def turnU(cube_matrix, isprime):
    if isprime == True:
        turnU(cube_matrix=cube_matrix, isprime=False)
        turnU(cube_matrix=cube_matrix, isprime=False)

    tempLC = cube_matrix[0][0][0] #Store white
    tempE = cube_matrix[0][0][1]
    tempRC = cube_matrix[0][0][2]

    cube_matrix[0][0][0] = cube_matrix[1][0][0] #Green to white
    cube_matrix[0][0][1] = cube_matrix[1][1][0]
    cube_matrix[0][0][2] = cube_matrix[1][2][0]

    cube_matrix[1][0][0] = cube_matrix[5][2][0] #Yellow to Green
    cube_matrix[1][1][0] = cube_matrix[5][2][1]
    cube_matrix[1][2][0] = cube_matrix[5][2][2]

    cube_matrix[5][2][0] = cube_matrix[3][0][2] #Blue to Yellow
    cube_matrix[5][2][1] = cube_matrix[3][1][2]
    cube_matrix[5][2][2] = cube_matrix[3][2][2]

    cube_matrix[3][0][2] = tempLC #White to Blue
    cube_matrix[3][1][2] = tempE
    cube_matrix[3][2][2] = tempRC

    temp_cube = cube_matrix
    for i in range(3):
        for j in range(3):
            cube_matrix[4][i][j] = temp_cube[4][j][2-i]

    return cube_matrix

def turnD(cube_matrix, isprime):
    if isprime == True:
        turnD(cube_matrix=cube_matrix, isprime=False)
        turnD(cube_matrix=cube_matrix, isprime=False)

    tempLC = cube_matrix[0][2][0] #Store white
    tempE = cube_matrix[0][2][1]
    tempRC = cube_matrix[0][2][2]

    cube_matrix[0][2][0] = cube_matrix[1][0][2] #Green to white
    cube_matrix[0][2][1] = cube_matrix[1][1][2]
    cube_matrix[0][2][2] = cube_matrix[1][2][2]

    cube_matrix[1][0][2] = cube_matrix[5][0][0] #Yellow to Green
    cube_matrix[1][1][2] = cube_matrix[5][0][1]
    cube_matrix[1][2][2] = cube_matrix[5][0][2]

    cube_matrix[5][0][0] = cube_matrix[3][0][0] #Blue to Yellow
    cube_matrix[5][0][1] = cube_matrix[3][1][0]
    cube_matrix[5][0][2] = cube_matrix[3][2][0]

    cube_matrix[3][0][0] = tempLC #White to Blue
    cube_matrix[3][1][0] = tempE
    cube_matrix[3][2][0] = tempRC

    temp_cube = cube_matrix
    for i in range(3):
        for j in range(3):
            cube_matrix[2][i][j] = temp_cube[4][j][2-i]

    return cube_matrix

def turnB(cube_matrix, isprime):
    

    temp_cube = cube_matrix
    for i in range(3):
        for j in range(3):
            cube_matrix[5][i][j] = temp_cube[5][j][2-i]
    return cube_matrix
"""
Variable Definitions:

cube_matrix - 
    this is a 3d array, consisting of face, row, column, to access the color
    color will be represented as number representing the order red->2 blue->3
    faces are organized as a 2d cube in this orientation
          []
        [][][][]
          []
    the faces, from top to bottom and left to right (in a solution scenario) are:
        white(0), green(1), red(2), blue(3), orange(4), yellow(5)
"""
def calculateTurns(cube_matrix):
    # oneDMat = [54]
    # ind = 0
    # for i in range(6):  #Working off of a pre-made image of a 1-D cube, theirs is set up slightly differently so converting is weird
    #     match i:
    #         case 0:
    #             ind = 9
    #         case 1:
    #             ind = 36
    #         case 2:
    #             ind = 0
    #         case 3:
    #             ind = 45
    #         case 4:
    #             ind = 18
    #         case 5:
    #             ind = 35
    #         case _:
    #             break
    #     if ind == 35: 
    #         for x in range(3):
    #             for y in range(3):
    #                 oneDMat[ind] = cube_matrix[i][x][y]
    #                 ind -= 1
    #     else:
    #         for x in range(3):
    #             for y in range(3):
    #                 oneDMat[ind] = cube_matrix[i][x][y]
    #                 ind += 1
        

    edgePositions = [4]
    edgeNum = 0
    for i in range(6):
        if cube_matrix[i][0][1] == 0:
            edgePositions[edgeNum] = [i, 0, 1]
            edgeNum += 1
        if cube_matrix[i][1][0] == 0:
            edgePositions[edgeNum] = [i, 1, 0]
            edgeNum += 1
        if cube_matrix[i][1][2] == 0:
            edgePositions[edgeNum] = [i, 1, 2]
            edgeNum += 1
        if cube_matrix[i][2][1] == 0:
            edgePositions[edgeNum] = [i, 2, 1]
            edgeNum += 1

        

    for edge in edgePositions:
        while edge != [0, 0, 1] or edge != [0, 2, 1] or edge != [0, 1, 2] or edge != [0, 1, 0]:
            if edge == [2, 1, 2]:
                turnR(cube_matrix=cube_matrix, isprime=True)
            if edge == [4, 1, 0]:
                turnR(cube_matrix=cube_matrix, isprime=False)
            if edge == [5, 1, 2]:
                turnR(cube_matrix=cube_matrix, isprime=False)
                turnR(cube_matrix=cube_matrix, isprime=False)
            
            if edge == [2, 1, 0]:
                turnL(cube_matrix=cube_matrix, isprime=True)
            if edge == [4, 1, 2]:
                turnL(cube_matrix=cube_matrix, isprime=False)
            if edge == [5, 1, 0]:
                turnL(cube_matrix=cube_matrix, isprime=False)
                turnL(cube_matrix=cube_matrix, isprime=False)

            if edge == [3, 1, 0]:
                turnD(cube_matrix=cube_matrix, isprime=True)
            if edge == [1, 1, 2]:
                turnD(cube_matrix=cube_matrix, isprime=False)
            if edge == [5, 0, 1]:
                turnD(cube_matrix=cube_matrix, isprime=False)
                turnD(cube_matrix=cube_matrix, isprime=False)
            
            if edge == [3, 0, 1]:
                turnU(cube_matrix=cube_matrix, isprime=True)
            if edge == [1, 1, 0]:
                turnU(cube_matrix=cube_matrix, isprime=False)
            if edge == [5, 2, 1]:
                turnU(cube_matrix=cube_matrix, isprime=False)
                turnU(cube_matrix=cube_matrix, isprime=False)

                    



