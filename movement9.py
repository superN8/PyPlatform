import sys
import pygame

GRID_SIZE = 600  # Pixels x Pixels of console size
SQ_NUM = 10  # Number of squares in grid
SQ_SIZE = GRID_SIZE / SQ_NUM  # Dimension of each square


# ===================================================================================

def create_level(lvl):
    grid = []
    while not grid:
        if lvl == 0:
            for row in range(0, SQ_NUM):
                column = []
                for col in range(0, SQ_NUM):
                    if row < SQ_NUM - 1:
                        column.insert(col, 0)
                    else:
                        column.insert(col, 1)
                grid.insert(row, column)

        elif lvl == 1:
            grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]]

        elif lvl == 2:
            grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]]

        elif lvl == 3:
            grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        elif lvl == 4:
            grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        elif lvl == 5:
            grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        lvl = 0
    return grid


# ===================================================================================

def draw_barrier(grid, sq_size, grid_size, surf):
    for i in range(0, grid_size):
        for ii in range(0, grid_size):
            if grid[i][ii] == 1:
                pygame.draw.rect(surf, (0, 100, 100), (sq_size * ii, sq_size * i, sq_size, sq_size))
            elif grid[i][ii] == 2:
                pygame.draw.rect(surf, (0, 255, 0), (sq_size * ii, sq_size * i, sq_size, sq_size))


# =====================================================================================

def corner_points(row, col):
    top_left = (col * SQ_SIZE, row * SQ_SIZE)
    top_right = (col * SQ_SIZE + SQ_SIZE, row * SQ_SIZE)
    bottom_left = (col * SQ_SIZE, row * SQ_SIZE + SQ_SIZE)
    bottom_right = (col * SQ_SIZE + SQ_SIZE, row * SQ_SIZE + SQ_SIZE)

    return [top_left, top_right, bottom_left, bottom_right]


# =====================================================================================

def get_cell(x, y):
    row = int(y / SQ_SIZE)
    col = int(x / SQ_SIZE)

    return row, col


# =====================================================================================

def get_direction(pair):
    direction = {
        (-1, -1): 1,  # Up and Left
        (0, -1): 2,  # Up
        (1, -1): 3,  # Up and Right
        (-1, 0): 4,  # Left
        (0, 0): 5,  # None
        (1, 0): 6,  # Right
        (-1, 1): 7,  # Down and left
        (0, 1): 8,  # Down
        (1, 1): 9  # Down and Right
    }
    return direction.get(pair, 8)


# =====================================================================================

def get_item(player, coord):
    # items = set({})
    # for i in range(0, len(GRID)):
    #    for ii in range(0, len(GRID[i])):
    #        if GRID[i][ii] == 2:
    #            items.add((i, ii))
    player.change_acc(1)


# =====================================================================================

class character:
    lives = 3
    acc = 1
    dec = 2
    speedMax = 10
    jumpSpeed = 10
    jumps = 2
    jumped = jumps
    gravity = .5
    color = (0, 200, 250)
    x = 0
    y = 0
    h = 60
    w = 30
    x_vel = 0
    y_vel = 0
    onePushUp = True  # extra attribute to help with multiple jumps

    # onePushDown = True

    def change_acc(self, n):
        self.acc += n
        return self.acc

    def move(self):

        xDir = 0
        yDir = 0
        self.y_vel += self.gravity
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if self.x_vel > 0:
                self.x_vel -= self.dec
            elif self.x_vel > -self.speedMax:
                self.x_vel -= self.acc
            else:
                self.x_vel = -self.speedMax

        if keys[pygame.K_RIGHT]:
            if self.x_vel < 0:
                self.x_vel += self.dec
            elif self.x_vel < self.speedMax:
                self.x_vel += self.acc
            else:
                self.x_vel = self.speedMax

        if self.x_vel != 0 and not (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]):
            if abs(self.x_vel) <= self.dec:
                self.x_vel = 0
            elif self.x_vel > 0:
                self.x_vel -= self.dec
            else:
                self.x_vel += self.dec

        if keys[pygame.K_UP]:
            if self.jumped > 0 and self.onePushUp:
                self.y_vel = -self.jumpSpeed
                self.jumped -= 1
                self.onePushUp = False
        else:
            self.onePushUp = True

        if self.x_vel > 0:
            xDir = 1
        elif self.x_vel < 0:
            xDir = -1
        if self.y_vel > 0:
            yDir = 1
        elif self.y_vel < 0:
            yDir = -1
        direction = get_direction((xDir, yDir))

        TL = (self.x + self.x_vel, self.y + self.y_vel)
        TR = (TL[0] + self.w, TL[1])
        BL = (TL[0], TL[1] + self.h)
        BR = (TR[0], BL[1])

        # Up and Left
        if direction == 1:
            goodX = 0 <= TL[0]
            goodY = 0 <= TL[1]
            if goodY:
                nextCell = get_cell(TR[0], TR[1])
                if GRID[nextCell[0]][nextCell[1]] == 1:
                    self.y_vel = 0
                    self.y = nextCell[0] * SQ_SIZE + SQ_SIZE
                    goodY = False
            else:
                self.y_vel = 0
                self.y = 0

            if goodX:
                nextCell = get_cell(BL[0], BL[1])
                if GRID[nextCell[0]][nextCell[1]] == 1:
                    self.x_vel = 0
                    self.x = nextCell[1] * SQ_SIZE + SQ_SIZE
                    goodX = False
            else:
                self.x_vel = 0
                self.x = 0

            if goodX and goodY:
                nextCell = get_cell(TL[0], TL[1])
                if GRID[nextCell[0]][nextCell[1]] == 1:
                    cellCorners = corner_points(nextCell[0], nextCell[1])
                    xDif = abs(TL[0] - cellCorners[3][0])
                    yDif = abs(TL[1] - cellCorners[3][1])
                    if xDif >= yDif:
                        self.y_vel = 0
                        self.y = cellCorners[3][1]
                    else:
                        self.x_vel = 0
                        self.x = cellCorners[3][0]

        # up
        elif direction == 2:
            if TL[1] > 0:
                nextCellR = get_cell(TR[0] - 1, TR[1])
                nextCellL = get_cell(TL[0], TL[1])
                if GRID[nextCellR[0]][nextCellR[1]] == 1 or GRID[nextCellL[0]][nextCellL[1]] == 1:
                    self.y_vel = 0
                    self.y = nextCellL[0] * SQ_SIZE + SQ_SIZE
            else:
                self.y_vel = 0
                self.y = 0

        # Up and Right
        elif direction == 3:
            goodX = TR[0] < GRID_SIZE
            goodY = 0 <= TR[1]
            if goodY:
                nextCell = get_cell(TL[0], TL[1])
                if GRID[nextCell[0]][nextCell[1]] == 1:
                    self.y_vel = 0
                    self.y = nextCell[0] * SQ_SIZE + SQ_SIZE
                    goodY = False
            else:
                self.y_vel = 0
                self.y = 0

            if goodX:
                nextCell = get_cell(BR[0], BR[1])
                if GRID[nextCell[0]][nextCell[1]] == 1:
                    self.x_vel = 0
                    self.x = nextCell[1] * SQ_SIZE - self.w
                    goodX = False
            else:
                self.x_vel = 0
                self.x = GRID_SIZE - self.w

            if goodX and goodY:
                nextCell = get_cell(TR[0], TR[1])
                if GRID[nextCell[0]][nextCell[1]] == 1:
                    cellCorners = corner_points(nextCell[0], nextCell[1])
                    xDif = abs(TR[0] - cellCorners[2][0])
                    yDif = abs(TR[1] - cellCorners[2][1])
                    if xDif >= yDif:
                        self.y_vel = 0
                        self.y = cellCorners[2][1]
                    else:
                        self.x_vel = 0
                        self.x = cellCorners[2][0] - self.w

        # Left
        elif direction == 4:
            if 0 < TL[0]:
                nextCell = get_cell(TL[0], TL[1])
                if GRID[nextCell[0]][nextCell[1]] == 1:
                    self.x_vel = 0
                    self.x = nextCell[1] * SQ_SIZE + SQ_SIZE
                else:
                    nextCell = get_cell(BL[0], BL[1])
                    if GRID[nextCell[0]][nextCell[1]] == 1:
                        self.x_vel = 0
                        self.x = nextCell[1] * SQ_SIZE + SQ_SIZE
            else:
                self.x_vel = 0
                self.x = 0

        # None
        # standing still direction == 5

        # Right
        elif direction == 6:
            if TR[0] < GRID_SIZE:
                nextCell = get_cell(TR[0], TR[1])
                if GRID[nextCell[0]][nextCell[1]] == 1:
                    self.x_vel = 0
                    self.x = nextCell[1] * SQ_SIZE - self.w
                else:
                    nextCell = get_cell(BR[0], BR[1])
                    if GRID[nextCell[0]][nextCell[1]] == 1:
                        self.x_vel = 0
                        self.x = nextCell[1] * SQ_SIZE - self.w
            else:
                self.x_vel = 0
                self.x = GRID_SIZE - self.w

        # down and left
        elif direction == 7:
            goodX = 0 <= BL[0]
            goodY = BL[1] < GRID_SIZE

            if goodY:
                nextCell = get_cell(BR[0], BR[1])
                if GRID[nextCell[0]][nextCell[1]] == 1:
                    self.y_vel = 0
                    self.y = nextCell[0] * SQ_SIZE - self.h
                    self.jumped = self.jumps
                    goodY = False
            elif TL[1] >= GRID_SIZE:
                self.x = 0
                self.y = 0
                self.y_vel = 0

            if goodX and TL[1] < GRID_SIZE:
                nextCell = get_cell(TL[0], TL[1])
                if GRID[nextCell[0]][nextCell[1]] == 1:
                    self.x_vel = 0
                    self.x = nextCell[1] * SQ_SIZE + SQ_SIZE
                    goodX = False
            elif not goodX:
                self.x_vel = 0
                self.x = 0

            if goodX and goodY:
                nextCell = get_cell(BL[0] - 1, BL[1])
                if GRID[nextCell[0]][nextCell[1]] == 1:
                    cellCorners = corner_points(nextCell[0], nextCell[1])
                    xDif = abs(BL[0] - cellCorners[1][0])
                    yDif = abs(BL[1] - cellCorners[1][1])
                    if xDif >= yDif:
                        self.y_vel = 0
                        self.y = cellCorners[0][1] - self.h
                        self.jumped = self.jumps
                    else:
                        self.x_vel = 0
                        self.x = cellCorners[1][0]

        # Down
        elif direction == 8:
            if BL[1] < GRID_SIZE:
                nextCellR = get_cell(BR[0] - 2, BR[1])
                nextCellL = get_cell(BL[0], BL[1])
                if GRID[nextCellR[0]][nextCellR[1]] == 1 or GRID[nextCellL[0]][nextCellL[1]] == 1:
                    self.y_vel = 0
                    self.y = nextCellL[0] * SQ_SIZE - self.h
                    self.jumped = self.jumps
            elif TL[1] >= GRID_SIZE:
                self.x = 0
                self.y = 0
                self.y_vel = 0

        # Down and Right
        elif direction == 9:
            goodX = BR[0] < GRID_SIZE
            goodY = BR[1] < GRID_SIZE
            if goodY:
                nextCell = get_cell(BL[0], BL[1])
                if GRID[nextCell[0]][nextCell[1]] == 1:
                    self.y_vel = 0
                    self.y = nextCell[0] * SQ_SIZE - self.h
                    self.jumped = self.jumps
                    goodY = False
            elif TL[1] >= GRID_SIZE:
                self.x = 0
                self.y = 0
                self.y_vel = 0

            if goodX and TL[1] < GRID_SIZE:
                nextCell = get_cell(TR[0], TR[1])
                if GRID[nextCell[0]][nextCell[1]] == 1:
                    self.x_vel = 0
                    self.x = nextCell[1] * SQ_SIZE - self.w
                    goodX = False
            elif not goodX:
                self.x_vel = 0
                self.x = GRID_SIZE - self.w

            if goodX and goodY:
                nextCell = get_cell(BR[0], BR[1])
                if GRID[nextCell[0]][nextCell[1]] == 1:
                    cellCorners = corner_points(nextCell[0], nextCell[1])
                    xDif = abs(BR[0] - cellCorners[0][0])
                    yDif = abs(BR[1] - cellCorners[0][1])
                    if xDif >= yDif:
                        self.y_vel = 0
                        self.y = cellCorners[0][1] - self.h
                        self.jumped = self.jumps
                    else:
                        self.x_vel = 0
                        self.x = cellCorners[0][0] - self.w
        moveX = self.x_vel != 0
        moveY = self.y_vel != 0
        if moveX:
            self.x += self.x_vel
        if moveY:
            self.y += self.y_vel
        if moveX or moveY:
            TL = (self.x, self.y)
            TR = (self.x + self.w, self.y)
            BL = (self.x, self.y + self.h)
            BR = (TR[0], BL[1])
            corners = [TL, TR, BL, BR]
            for i in range(0, len(corners)):
                # corner = {0: "TL", 1: "TR", 2: "BL", 3: "BR"}
                # print(corner.get(i))
                tempCell = get_cell(corners[i][0], corners[i][1])
                if GRID[tempCell[0]][tempCell[1]] == 2:
                    get_item(self, tempCell)


# =====================================================================================


# Boiler plate startup stuff
pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()
pygame.display.set_caption('Just a Test')

# Generate the grid to be used in the game loop
level = 5
GRID = create_level(level)
# quality of life improvement
pygame.key.set_repeat()

next_lvl = False
player = character()
# Main game loop
screen = pygame.display.set_mode((GRID_SIZE, GRID_SIZE))
while True:
    player.move()

    if next_lvl and level <= 5:  # 2 because 2 is currently the highest level
        level += 1
        GRID = create_level(level)
        next_lvl = False

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((200, 255, 255))  # Fill the surface background with the RGB color
    draw_barrier(GRID, SQ_SIZE, SQ_NUM, screen)
    if player.lives > 0:
        pygame.draw.rect(screen, player.color, (player.x, player.y, player.w, player.h))

    # Advance the game counter
    pygame.display.update()
    fpsClock.tick(FPS)
