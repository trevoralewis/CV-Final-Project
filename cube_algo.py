
def turnR(cube_matrix, isprime):
    return cube_matrix

def turnL(cube_matrix, isprime):
    return cube_matrix

def turnF(cube_matrix, isprime):
    return cube_matrix

def turnU(cube_matrix, isprime):
    return cube_matrix

def turnD(cube_matrix, isprime):
    return cube_matrix

def turnB(cube_matrix, isprime):
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
    print(cube_matrix)