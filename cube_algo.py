
test_cube = [
    [[1,5,3],[5,0,5],[1,0,0]],
    [[4,4,5],[1,1,4],[2,0,1]],
    [[2,2,3],[0,2,3],[0,4,5]],
    [[4,3,0],[0,3,2],[4,5,4]],
    [[2,1,0],[3,4,2],[5,4,5]],
    [[2,3,1],[1,5,2],[3,1,3]],
]

def turnR(cube_matrix, isprime):
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
    tempLC = cube_matrix[0][0][0] #Store white
    tempE = cube_matrix[0][0][1]
    tempRC = cube_matrix[0][0][2]

    cube_matrix[0][0][0] = cube_matrix[1][0][0] #Green to white
    cube_matrix[0][0][1] = cube_matrix[1][0][1]
    cube_matrix[0][0][2] = cube_matrix[1][0][2]

    cube_matrix[1][0][0] = cube_matrix[5][0][0] #Yellow to Green
    cube_matrix[1][0][1] = cube_matrix[5][0][1]
    cube_matrix[1][0][2] = cube_matrix[5][0][2]

    cube_matrix[5][0][0] = cube_matrix[3][0][0] #Blue to Yellow
    cube_matrix[5][0][1] = cube_matrix[3][0][1]
    cube_matrix[5][0][2] = cube_matrix[3][0][2]

    cube_matrix[3][0][0] = tempLC #White to Blue
    cube_matrix[3][0][1] = tempE
    cube_matrix[3][0][2] = tempRC

    temp_cube = cube_matrix
    for i in range(3):
        for j in range(3):
            cube_matrix[4][i][j] = temp_cube[4][j][2-i]

    return cube_matrix

def turnD(cube_matrix, isprime):
    tempLC = cube_matrix[0][2][0] #Store white
    tempE = cube_matrix[0][2][1]
    tempRC = cube_matrix[0][2][2]

    cube_matrix[0][2][0] = cube_matrix[1][2][0] #Green to white
    cube_matrix[0][2][1] = cube_matrix[1][2][1]
    cube_matrix[0][2][2] = cube_matrix[1][2][2]

    cube_matrix[1][2][0] = cube_matrix[5][2][0] #Yellow to Green
    cube_matrix[1][2][1] = cube_matrix[5][2][1]
    cube_matrix[1][2][2] = cube_matrix[5][2][2]

    cube_matrix[5][2][0] = cube_matrix[3][2][0] #Blue to Yellow
    cube_matrix[5][2][1] = cube_matrix[3][2][1]
    cube_matrix[5][2][2] = cube_matrix[3][2][2]

    cube_matrix[3][2][0] = tempLC #White to Blue
    cube_matrix[3][2][1] = tempE
    cube_matrix[3][2][2] = tempRC

    temp_cube = cube_matrix
    for i in range(3):
        for j in range(3):
            cube_matrix[2][i][j] = temp_cube[2][j][2-i]

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
    while cube_matrix[0][0][1] != cube_matrix[0][1][1]:
        turnU(cube_matrix=cube_matrix, isprime=False)
    while cube_matrix[0][1][0] != cube_matrix[0][1][1]:
        turnL(cube_matrix=cube_matrix, isprime=False)
    while cube_matrix[0][1][2] != cube_matrix[0][1][1]:
        turnR(cube_matrix=cube_matrix, isprime=False)
    while cube_matrix[0][2][1] != cube_matrix[0][1][1]:
        turnD(cube_matrix=cube_matrix, isprime=False)
