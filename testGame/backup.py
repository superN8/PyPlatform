import sys
import pygame

# Define some constants
x_pos = 0  # Player initial x position
y_pos = 0  # Player initial y position
GRID_SIZE = 600  # Pixels x Pixels of console size
SQ_NUM = 10  # Number of squares in grid
SQ_SIZE = GRID_SIZE / SQ_NUM  # Dimension of each square
level = 2


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

        if lvl == 5:
            for row in range(0, SQ_NUM):
                column = []
                for col in range(0, SQ_NUM):
                    if row < SQ_NUM - 2 or not ((col % 2) + (row % 2) == 1):
                        column.insert(col, 0)
                    else:
                        column.insert(col, 1)
                grid.insert(row, column)

        elif lvl == 6:
            grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        lvl = 0
    return grid


# ===================================================================================

def draw_barrier(grid, sq_size, grid_size, surf):
    for i in range(0, grid_size):
        for ii in range(0, grid_size):
            if grid[i][ii] == 1:
                pygame.draw.rect(surf, (0, 100, 100), (sq_size * ii, sq_size * i, sq_size, sq_size))


# =====================================================================================

def corner_points(row, col):
    top_left = (col * SQ_SIZE, row * SQ_SIZE)
    top_right = (top_left[0] + SQ_SIZE, top_left[1])
    bottom_left = (top_left[0], top_left[1] + SQ_SIZE)
    bottom_right = (top_right[0], bottom_left[1])

    return [top_left, top_right, bottom_left, bottom_right]


# =====================================================================================

def get_cell(x, y):
    row = int(y / SQ_SIZE)
    col = int(x / SQ_SIZE)

    return row, col


# =====================================================================================

def sign(n):
    if n > 0:
        return 1
    if n < 0:
        return -1
    return 0


# =====================================================================================

class character:
    lives = 3
    acc = 1  # ------------ acceleration
    dec = 2  # ------------ deceleration
    speedMax = 5  # ------- max speed
    slide = 3  # ---------- slide speed
    onePushDown = True  # - extra attribute to help with sliding
    gravity = .5  # ------- downward acceleration (fall speed)
    jumpSpeed = 10  # ----- initial speed of a jump (jump height)
    jumps = 2  # ---------- total jumps allowed
    jumped = jumps  # ----- jumps remaining
    onePushUp = True  # --- extra attribute to help with multiple jumps
    color = (0, 200, 250)
    x = 0
    y = 0
    h = 60
    w = 30
    x_vel = 0
    y_vel = 0

    def change_acc(self, n):
        self.acc += n
        return self.acc

    def respawn(self):
        self.x = 0
        self.x_vel = 0
        self.y = 0
        self.y_vel = 0
        # self.lives -= 1

    def set_color(self, c: tuple):
        self.color = c

    def move(self):

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

        if keys[pygame.K_DOWN] and self.y_vel >= 0:
            if self.onePushDown:
                temp = self.h
                self.h = self.w
                self.w = temp
                self.onePushDown = False
                self.speedMax += self.slide

        elif not self.onePushDown:
            temp = self.h
            self.h = self.w
            self.w = temp
            self.onePushDown = True
            self.speedMax -= self.slide
            self.y -= self.h / 2
            if self.x_vel > 0:
                self.x += self.h / 2

        TL = (self.x + self.x_vel, self.y + self.y_vel)
        TR = (TL[0] + self.w, TL[1])
        BL = (TL[0], TL[1] + self.h)
        BR = (TR[0], BL[1])
        nextCorners = (TL, TR, BL, BR)

        for cNum in range(0, 4):
            goodX = False
            goodY = False
            xDir = sign(self.x_vel)
            yDir = sign(self.y_vel)
            corner = nextCorners[cNum]

            if xDir != 0:
                goodX = 0 <= corner[0] < GRID_SIZE
            if yDir != 0:
                goodY = 0 <= corner[1] < GRID_SIZE

            if goodX:
                tempY = self.y + ((self.h - 1) * (cNum >= 2))
                if 0 <= tempY < GRID_SIZE:
                    nextCell = get_cell(corner[0], tempY)
                    if GRID[nextCell[0]][nextCell[1]] == 1:
                        goodX = False
                        right = xDir == 1
                        self.x_vel = 0
                        self.x = (nextCell[1] + (not right)) * SQ_SIZE - (self.w * right)
            else:
                self.x_vel = 0
                if corner[0] >= GRID_SIZE:
                    self.x = GRID_SIZE - self.w
                elif corner[0] < 0:
                    self.x = 0

            if goodY:
                tempX = self.x + ((self.w - 1) * (cNum % 2 == 1))
                if 0 <= tempX < GRID_SIZE:
                    nextCell = get_cell(tempX, corner[1])
                    if GRID[nextCell[0]][nextCell[1]] == 1:
                        goodY = False
                        self.y_vel = 0
                        down = yDir == 1
                        self.y = (nextCell[0] + (not down)) * SQ_SIZE - (self.h * down)
                        self.jumped = self.jumps
            else:
                if yDir == -1:
                    self.y_vel = 0
                    self.y = 0
                elif yDir == 1:
                    if TL[1] >= GRID_SIZE:
                        self.respawn()

            if goodX and goodY:
                nextCell = get_cell(corner[0], corner[1])
                if GRID[nextCell[0]][nextCell[1]] == 1:
                    cellCorners = corner_points(nextCell[0], nextCell[1])
                    xDif = abs(corner[0] - cellCorners[3 - cNum][0])
                    yDif = abs(corner[1] - cellCorners[3 - cNum][1])
                    if xDif >= yDif:
                        self.y_vel = 0
                        self.jumped = self.jumps
                        down = yDir == 1
                        self.y = (nextCell[0] + (not down)) * SQ_SIZE - (self.h * down)
                    else:
                        self.x_vel = 0
                        right = xDir == 1
                        self.x = (nextCell[1] + (not right)) * SQ_SIZE - (self.w * right)

        self.x += self.x_vel
        self.y += self.y_vel


# =====================================================================================


# Startup stuff
pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()
pygame.display.set_caption('Just a Test')

# Generate the grid to be used in the game loop

GRID = create_level(level)
# quality of life improvement
pygame.key.set_repeat()

next_lvl = False
player = character()
# Main game loop
screen = pygame.display.set_mode((GRID_SIZE, GRID_SIZE))
# i = 0
while True:
    player.move()

    # next_lvl = player.x >= GRID_SIZE - player.w - 1
    if next_lvl and level <= 1:
        level += 1
        GRID = create_level(level)
        player.respawn()
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
