import random
import pygame



pygame.init()
width = 400
height = 400
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((width, height))
screen.fill(WHITE)
w = width / 4
for i in range(4):
    for j in range(4):
        rect = pygame.Rect(i * w, j * w, w, w)
        pygame.draw.rect(screen, BLACK, rect, 1)

grid = [[0, 0, 0, 0],
        [0, 0, 2, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

def drawGrid(screen):
    for i in range(4):
        for j in range(4):
            font = pygame.font.Font(None, 50)
            text = font.render(str(grid[i][j]), True, BLACK)
            textRect = text.get_rect()
            newRect = pygame.Rect(i * 100 + 1, j * 100 + 1, 98, 98)
            textRect.center = ((i * 100) + 50, (j * 100) + 50)
            screen.fill(WHITE, newRect)
            if grid[i][j] != 0:
                screen.blit(text, textRect)

def checkGrid(matrix):
    going = False
    for i in matrix:
        for j in i:
            if j == 0:
                going = True
    return going

def addNumber():
    if random.randint(0,1) == 0:
        num = 2
    else:
        num = 4
    running = True
    while running:
        rani = random.randint(0,3)
        ranj = random.randint(0,3)
        if grid[rani][ranj] == 0:
            grid[rani][ranj] = num
            running = False


def slideDown(list):
    a = [val for val in list if val > 0]
    miss = 4 - len(a)
    misslist = []
    for i in range(miss):
        misslist.append(0)
    arr = misslist + a
    return arr


def combineDown(list):
    for i in range(len(list) - 1, 0, -1):
        a = list[i]
        b = list[i - 1]
        if a == b:
            list[i] = list[i] + list[i - 1]
            list[i - 1] = 0


def flipGrid():
    for i in grid:
        i.reverse()


def emptyGrid():
    return [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]


def rotateLeft():
    global grid
    tempGrid = emptyGrid()
    for i in range(4):
        for j in range(4):
            tempGrid[i][j] = grid[j][3 - i]
    grid = tempGrid


def rotateRight():
    global grid
    tempGrid = emptyGrid()
    for i in range(4):
        for j in range(4):
            tempGrid[i][3-j] = grid[j][i]
    grid = tempGrid


def movement(matrix):
    for i in range(len(matrix)):
        matrix[i] = slideDown(matrix[i])
        combineDown(matrix[i])
        matrix[i] = slideDown(matrix[i])


def updatePastGrid():
    global pastGrid
    pastGrid = grid


def operation(str):
    global grid
    if str == "DOWN":
        movement(grid)
    if str == "UP":
        flipGrid()
        movement(grid)
        flipGrid()
    if str == "LEFT":
        rotateRight()
        movement(grid)
        rotateLeft()
    if str == "RIGHT":
        rotateLeft()
        movement(grid)
        rotateRight()

    if checkGrid(grid):
        addNumber()
    else:
        print("YOU LOSE!")
        pygame.quit()



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            operation('DOWN')
        if key[pygame.K_UP]:
            operation("UP")
        if key[pygame.K_LEFT]:
            operation("LEFT")
        if key[pygame.K_RIGHT]:
            operation("RIGHT")
        if key[pygame.K_ESCAPE]:
            pygame.quit()

    drawGrid(screen)

    pygame.display.update()
pygame.quit()
