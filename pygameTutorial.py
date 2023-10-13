import pygame
import tkinter as tk

pygame.init()

screenWidth, screenHeight = 500, 500

win = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("PyGame 1")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

x = 50
y = 425
width = 64
height = 64
vel = 10

clock = pygame.time.Clock()


def redrawWin():
    global walkCount
    win.blit(bg, (0, 0))
    if walkCount + 1 >= 27:
        walkcount = 0
    if left:
        win.blit(walkLeft[walkCount // 3], (x, y))
        walCount += 1
    elif right:
        win.blit(walkRight[walkCount // 3], (x, y))
    pygame.display.update()


# main
run = True
while run:
    clock.tick(27)
    pygame.time.delay(50)

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
        left = False
        right = True
    else:
        left = False
        right = False
        walkCount = 0
    if not isJump:
        '''if keys[pygame.K_UP] and y > vel:
                 y -= vel
           if keys[pygame.K_DOWN] and y < screenWidth - height - vel:
                 y += vel'''
    if keys[pygame.K_SPACE]:
        isJump = True
        left = False
        right = False
        walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    redrawWin()
pygame.quit()
