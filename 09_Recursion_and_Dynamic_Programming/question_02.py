import numpy as np
import math
from math import factorial as ff
np.set_printoptions(linewidth=200)

def question_02(x,y):
    result = np.ones((x,y), dtype=np.int) # Takes care of first row and first col
    for xi in range(1,x):
        for yi in range(1,y):
            result[xi,yi] = result[xi-1,yi] + result[xi,yi-1] 
    return result   

def num_paths(x,y):
    # list of x items, each of which are lists of length y
    paths = [[1 for _ in range(y+1)] for _ in range(x+1)]
    # Skip over first row and first col as we know those are are 1.
    for row in range(1,x+1):
        for col in range(1,y+1):
            paths[row][col] = paths[row-1][col]+paths[row][col-1]
    print(np.array(paths))
    return paths[x][y] 


if __name__ == "__main__":
    #grid = question_02(2,2)
    #print(grid)
    #print("")
    #grid = question_02(15,10)
    #print(grid)

    print("\n\n2017\n\n")
    print(num_paths(2,2))
    print(num_paths(15,10))
    print( ff(15+10)/(ff(15)*ff(10)) )
