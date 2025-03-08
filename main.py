import pygame
import random
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('SkibidiCatcher')
clock = pygame.time.Clock()


ballspos = [50,120,160,100,180,230,260,270,300,320,360,400,440,500,520]
randomint = random.randint(0,14)

heartpos = [-10,70,150]


#fonts
text_font1 = pygame.font.SysFont("Arial",30)

#important variables
showplay = True
showcatcher = False
showballs = False
ballgravity = 0
toggleinfopress = 1
score = 0
hearts = 3
endlessballspeed = 0.6

#asset loading/defining
menubg = pygame.image.load("img/menubg.jpg")
menubgrect = menubg.get_rect(topleft=(0,0))

playbutton = pygame.image.load("img/playbutton.png")
playbutton_rect = playbutton.get_rect(topleft=(220,130))

catcher = pygame.image.load("img/catcher.png")

ball = pygame.image.load("img/ball.png")
ball_rect = ball.get_rect(topleft=(120,-10))

heart = pygame.image.load("img/heart.png")
heart_rect = heart.get_rect(topleft=(-10,500))

endscreen = pygame.image.load("img/endscreen.png")
endscreen_rect = endscreen.get_rect(topleft=(0,0))

restartbutton = pygame.image.load("img/restart.png")
restartbutton_rect = restartbutton.get_rect(topleft=(300,400))


#my functions
def ballreset():
    global ballgravity
    global randomint
    randomint = random.randint(0,14)
    ball_rect.x = ballspos[randomint]
    ball_rect.y = -10
    ballgravity = 0

def drawtext(text,font,textcol,x,y):
    image = font.render(text,True,textcol)
    screen.blit(image,(x,y))

#Classes

class Catcher:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rect = catcher.get_rect(topleft=(self.x,self.y))

    def important(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def moveboundaries(self):
        if self.x < -10:
            self.x = -10
        if self.x > 700:
            self.x = 700

       

#object defining
catcher1 = Catcher(320,450)

running = True
while running:
    mousepos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if playbutton_rect.collidepoint(mousepos):
                showplay = False
                showcatcher = True
                showballs = True
            if restartbutton_rect.collidepoint(mousepos):
                showplay = True
                hearts = 3
                heartpos = [-10,70,150]
                score = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                toggleinfopress += 1


    #some object functions
    catcher1.important()
    catcher1.moveboundaries()

    #moving code
    if keys[pygame.K_a]:
        catcher1.x -= 10
    if keys[pygame.K_d]:
        catcher1.x += 10

    
    screen.fill((0,0,0))
    screen.blit(menubg,menubgrect)
    if showplay == True:
        screen.blit(playbutton,playbutton_rect)
    if showcatcher == True:
        screen.blit(catcher,catcher1.rect)
    if showballs == True:
        if ball_rect.y > 500:            
            ballreset()
            hearts -= 1
            if hearts > -1:
                heartpos.pop()
            if hearts == 0:
                showballs = False
                showcatcher = False
                showplay = False
        if ball_rect.colliderect(catcher1.rect):
            ballreset()
            score += 1
        ball_rect.x = ballspos[randomint]
        ballgravity += endlessballspeed
        ball_rect.y += ballgravity
        screen.blit(ball,ball_rect)
    if toggleinfopress == 1 and showcatcher == True:
        drawtext(str(score),text_font1, (0,0,0), 750,5)
    elif toggleinfopress == 2:
        toggleinfopress = 0
    if showcatcher == True:
        for l in heartpos:
            heart_rect.x = l
            screen.blit(heart,heart_rect)
    if hearts == 0:
        screen.blit(endscreen,endscreen_rect)
        screen.blit(restartbutton,restartbutton_rect)
    pygame.display.flip()
    clock.tick(60)
