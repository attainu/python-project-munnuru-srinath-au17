class BackTracking():
    def __init__(self, rows):
        self.rows = rows

    def printSolution(self, sol):
        return sol

    def isSafe(self, maze, x, y):
        if x >= 0 and x < self.rows and y >= 0 and y < self.rows and maze[x][y] == 1:
            return True
        return False

    def solveMaze(self, maze):
        sol = [[0 for j in range(self.rows)] for i in range(self.rows)]
        if self.solveMazeUtil(maze, 0, 0, sol) is False:
            return -1
        sol = self.printSolution(sol)
        return sol

    def solveMazeUtil(self, maze, x, y, sol):
        if x == self.rows - 1 and y == self.rows - 1 and maze[x][y] == 1:
            sol[x][y] = 1
            return True
        if self.isSafe(maze, x, y) is True:
            if sol[x][y] == 1:
                return False
            sol[x][y] = 1
            if self.solveMazeUtil(maze, x + 1, y, sol) is True:
                return True
            if self.solveMazeUtil(maze, x, y + 1, sol) is True:
                return True
            if self.solveMazeUtil(maze, x - 1, y, sol) is True:
                return True
            if self.solveMazeUtil(maze, x, y - 1, sol) is True:
                return True
            sol[x][y] = 0
            return False
