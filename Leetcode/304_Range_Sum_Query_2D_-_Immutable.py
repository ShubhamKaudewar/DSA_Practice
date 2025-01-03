from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMatrix = [[0] * (COLS+1) for _ in range(ROWS+1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMatrix[r][c+1]
                self.sumMatrix[r+1][c+1] = prefix + above

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        r1, c1, r2, c2 = r1+1, c1+1, r2+1, c2+1

        bottomRight =self.sumMatrix[r2][c2]
        above = self.sumMatrix[r1-1][c2]
        left = self.sumMatrix[r2][c1-1]
        topLeft = self.sumMatrix[r1-1][c1-1]

        return bottomRight - left - above + topLeft

if __name__ == '__main__':
    nm, output = None, [None]
    inps = ["NumMatrix","sumRegion","sumRegion","sumRegion"]
    val_inps = [
        [[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],
        [2,1,4,3],
        [1,1,2,2],
        [1,2,2,4]
    ]
    for inp, val_inp in zip(inps, val_inps):
        if inp == "NumMatrix":
            nm = NumMatrix(*val_inp)
        else:
            res = nm.sumRegion(*val_inp)
            output.append(res)
    print(output)