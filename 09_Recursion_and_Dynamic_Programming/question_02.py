import numpy as np

def question_02(x,y):
    result = np.ones((x,y), dtype=np.int) # Takes care of first row and first col
    for xi in range(1,x):
        for yi in range(1,y):
            result[xi,yi] = result[xi-1,yi] + result[xi,yi-1] 
    return result   

if __name__ == "__main__":
    grid = question_02(2,2)
    print(grid)
    print("")
    grid = question_02(15,10)
    print(grid)
