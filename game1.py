import pygame
import math
import random

pygame.init()

# createing a screen
screen = pygame.display.set_mode((960, 640))

# title and caption
pygame.display.set_caption("SPACE INVADERS")
icon = pygame.image.load('project.png')
pygame.display.set_icon(icon)

# background
back = pygame.image.load('back (1).png')

# player
playerim = pygame.image.load('player.png')
px = 448
py = 512
pdx = 0
pdy = 0

# bullet
bullim = pygame.image.load('bullet.png')
bx = 0
by = 0
bdy = 2
bstate = "ready"

# enemy
enemyim = pygame.image.load('ufo.png')
ex = random.randint(0, 896)
ey = random.randint(0, 256)
edx = 1
edy = random.randint(32, 128)


# player function
def player(x, y):
    screen.blit(playerim, (x - 16, y + 16))


# enemy function
def enemy(x, y):
    screen.blit(enemyim, (x, y))


# bullet function
def bfire(x, y):
    global bstate
    bstate = "fire"
    screen.blit(bullim, (x, y))

# collision
def collision(x, y, p, q):
    dist = math.sqrt((math.pow(x - p, 2)) + math.pow(y - q, 2))
    if dist < 32:
        return True
    else:
        return False

def collision_2(x, y, p, q):
    dist = math.sqrt((math.pow(x - p, 2)) + math.pow(y - q, 2))
    if dist < 64:
        return True
    else:
        return False


# scoring
score = 0
s_font = pygame.font.Font('freesansbold.ttf',24)

def scoreboard():
    s_text  = s_font.render("Score :" + str(score), True, (255,255,255))
    screen.blit(s_text,(10,10))
    print(score)
# game over
over_font = pygame.font.Font('freesansbold.ttf', 128)


def gameover():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (100, 188))
    print("game over")

flag = 1
# quit event (loop makes sure that game is running till close button is pressed)
run = True
while run:

    # BACKGROND COLOR ( RGB)
    screen.fill((42, 15, 73))
    screen.blit(back, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pdx = -1
            if event.key == pygame.K_RIGHT:
                pdx = +1
            if event.key == pygame.K_UP:
                pdy = -1
            if event.key == pygame.K_DOWN:
                pdy = +1
            if event.key == pygame.K_SPACE:
                if bstate == "ready":
                    bx = px
                    by = py
                    bfire(bx, by)
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT or event.key == pygame.K_UP) and (
                    event.key == pygame.K_LEFT or event.key == pygame.K_DOWN):
                pdx = 0
                pdy = 0
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_UP) and (
                    event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN):
                pdx = 0
                pdy = 0
            if (event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                pdy = 0

    px += pdx
    if px <= 0:
        px = 0
    elif px >= 896:
        px = 896

    py += pdy
    if py <= 320:
        py = 320
    elif py >= 576:
        py = 576

    q = (score/1000)
    ex += edx
    if ex <= 0:
        edx = (0.8+q)
        ey += edy
    elif ex >= 896:
        edx = -(0.8+q)
        ey += edy
    if ey <= 0:
        edy = -edy
        ey += edy
    elif ey >= 512:
        edy = -edy
        ey += edy
    # bullet movement
    if by <= 0:
        by = py
        bstate = "ready"

    if bstate == "fire":
        bfire(bx, by)
        by -= bdy

    # hit
    hit = collision(ex + 32, ey + 32, bx + 16, by + 16)
    if hit == True:
        by = py
        bstate = "ready"
        score += 10
        ex = random.randint(0, 896)
        ey = random.randint(0, 256)
    scoreboard()

    # gameover

    if flag == 1:
        game = collision_2(ex + 32, ey + 32, px + 32, py + 32)
    if game==True:
        ex = 2000
        ey = 2000
        px = 448
        py = 512
        gameover()
        flag = 0



    # player function called
    player(px, py)

    # enemy function called
    enemy(ex, ey)

    pygame.display.update()
