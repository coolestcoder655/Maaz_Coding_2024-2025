import turtle
import asyncio

pen = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("white")
pen.speed(10)
pen.hideturtle()
player = turtle.Turtle()
player.color("blue")
player.hideturtle()
walls = set()
win = set()


mazeWidth = 300
mazeHeight = 300

def moveSpace(spaces: int):
    pen.up()
    pen.forward(spaces)
    pen.down()

def drawSquare(sideLength: int, color: str = "black", **kwargs):
    pen.color(color)
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(4):
        for _ in range(sideLength):
            pen.forward(1)
            if kwargs.get("isWin", False) == True:
                win.add(pen.position())
                print(pen.position())
            

        pen.right(90)
    pen.end_fill()
    pen.color("black")


def drawMaze(maze: list[str], startingCoords: tuple[int, int]):
    startX = startingCoords[0]
    startY = startingCoords[1]
    pen.up()
    pen.goto(startX, startY)
    pen.down()
    for row in maze:
        for char in row:
            if char == "s":
                drawSquare(10, "green")
                moveSpace(20)
                startPos = pen.position()
                print(f"Start Position: {startPos}")
            elif char == "e":
                drawSquare(10, "red", isWin=True)
                moveSpace(20)
                endPos = pen.position()
                print(f"End Position: {endPos}")
            elif char == " ":
                moveSpace(20)
            elif char == "x":
                pen.forward(10)
                walls.add(pen.position())
                pen.forward(10)

            pen.fillcolor("black")
            
        pen.up()
        pen.goto(startX, startY - 20)
        startY = startY - 20
        pen.down()

    return (startPos, endPos)


def startMaze(maze: list[str], startCoords: tuple[int, int]):
    startPos, endPos = drawMaze(maze, startCoords)
    startX = startCoords[0]
    startY = startCoords[1]
    player.up()
    player.goto(startPos[0], startPos[1] - 5)
    player.down()
    player.showturtle()
    screen.onkeypress(moveUp, "Up")
    screen.onkeypress(moveDown, "Down")
    screen.onkeypress(moveLeft, "Left")
    screen.onkeypress(moveRight, "Right")
    screen.listen()




def moveUp():
    player.setheading(90)
    if not validMove((player.pos() + (0, 5))):
        return
    
    player.forward(5)

def moveDown():
    player.setheading(270)
    if not validMove((player.pos() + (0, -5))):
        return
    
    player.forward(5)

def moveLeft():
    player.setheading(180)
    if not validMove((player.pos() + (-5, 0))):
        return
    
    player.forward(5)

def moveRight():
    player.setheading(0)
    if not validMove((player.pos() + (5, 0))):
        return
    
    player.forward(5)

mazeDesign = [
        "xxxxxxxxxxxxxxxxxx",
        "xs      x        x",
        "xxxx xx x xxxxxxxx",
        "x    xx x x      x",
        "xxxx xx x x xxxxxx",
        "x    xx x x x    x",
        "xxxx xx x x x xxxx",
        "x    xx x x x    x",
        "xxxx xx x x x  xxx",
        "x    xx   x x    x",
        "xxxx xxxxxxxxxxxxx",
        "x                e",
        "xxxxxxxxxxxxxxxxxx"
    ]

def validMove(moveTo: tuple[int, int]):
    x = moveTo[0]
    y = moveTo[1]

    if ((x + 5, y) in walls) or ((x - 5, y) in walls):
        return False
    
    print(player.pos())

    if player.pos() in win:
        turtle.bye()
        print("YOU HAVE WINNED THE GAME" + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" * 100)
    
    print((player.pos()) in walls)
    return True

try:
    startMaze(mazeDesign, (-120, 200))
except Exception as e:
    print(e)

screen.exitonclick()