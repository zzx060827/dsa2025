import turtle
OBSTACLE = '+'
TRIED = '#'
DEAD_END = '$'
PART_OF_PATH = '*'
TURTLE = 'S'
class Maze(list):
    def __init__(self, mazeFileName):
        self.columnsInMaze = 0
        mazeFile = open(mazeFileName, 'r')
        for line in mazeFile:
            rowList = []
            for col, ch in enumerate(line[:-1]):
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = len(self)
                    self.startCol = col
            self.append(rowList)
            if self.columnsInMaze == 0 :
                self.columnsInMaze = len(rowList)
            else:  #对输入数据进行检查
                assert self.columnsInMaze == len(rowList)
        self.t = turtle.Turtle()
        self.w = turtle.Screen()

    def updatePosition(self, row, col, what):
        self[row][col] = what
        self.draw_cell(row, col)

    def draw_cell(self, row, col, size=40):
        what = self[row][col]
        if what == OBSTACLE:
            self.drawSquare((col*size, row*size), size, "orange")
        elif what == TURTLE:
            self.drawSquare((col*size, row*size), size, "white")
            self.drawSquare((col*size+10, row*size+10), 20, "green")
        elif what == TRIED:
            self.drawSquare((col*size, row*size), size, "white")
            self.drawSquare((col*size+15, row*size+15), 10, "blue")
        elif what == DEAD_END:
            self.drawSquare((col*size, row*size), size, "white")
            self.drawSquare((col*size+15, row*size+15), 10, "black")
        elif what == PART_OF_PATH:
            self.drawSquare((col*size, row*size), size, "white")
            self.drawFlag((col*size+15, row*size+15), 10, "red")
        else:
            self.drawSquare((col*size, row*size), size, "white")

    def isExit(self, row, col):
        return row == 0 or row == len(self)-1 \
                or col == 0 or col == self.columnsInMaze-1
    def draw(self):
        for row in range(len(self)):
            for col in range(self.columnsInMaze):
                self.draw_cell(row, col)
        return True
    def t_goto(self, x, y):
        self.t.goto(x-200, 200-y)

    def drawFlag(self, start, size, color):
        self.t.fillcolor(color)
        self.t.up()
        self.t_goto(start[0], start[1])
        self.t.down()
        self.t.begin_fill()
        self.t_goto(start[0]+size, start[1])
        self.t_goto(start[0], start[1]+size)
        self.t_goto(start[0], start[1])
        self.t.end_fill()
        self.t.right(90)
        self.t.forward(size/3)
        self.t.backward(size/3)
        self.t.left(90)

    def drawSquare(self, start, size, color):
        self.t.fillcolor(color)
        self.t.up()
        self.t_goto(start[0], start[1])
        self.t.down()
        self.t.begin_fill()
        self.t_goto(start[0]+size, start[1])
        self.t_goto(start[0]+size, start[1]+size)
        self.t_goto(start[0], start[1]+size)
        self.t_goto(start[0], start[1])
        self.t.end_fill()

    def search_exit(self):
        self.searchFrom(self.startRow, self.startCol)

    def searchFrom(self, startRow, startColumn):
        if self[startRow][startColumn] == OBSTACLE :
            return False
        if self[startRow][startColumn] == TRIED or self[startRow][startColumn] == DEAD_END :
            return False
        self.updatePosition(startRow, startColumn, TURTLE)
        if self.isExit(startRow, startColumn):
            #self.updatePosition(startRow, startColumn, PART_OF_PATH)
            return True
        self.updatePosition(startRow, startColumn, TRIED)
        found = self.searchFrom(startRow-1, startColumn) or \
            self.searchFrom(startRow+1, startColumn) or \
            self.searchFrom(startRow, startColumn-1) or \
            self.searchFrom(startRow, startColumn+1) 
        if found:
            self.updatePosition(startRow, startColumn, PART_OF_PATH)
        else:
            self.updatePosition(startRow, startColumn, DEAD_END)
        return found
    def exit(self):
        self.w.exitonclick()

import sys

if __name__ == "__main__":
    #mazefile = input("Pls input maze filename")
    mazefile = sys.path[0]+"/maze.txt"
    maze = Maze(mazefile)
    maze.draw()
    maze.search_exit()
    maze.exit()
