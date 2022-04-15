#Imports
import pygame, time
from pygame.locals import *
from random import randint
 
pygame.init() #Initialzing 
    
#Setting up FPS 
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
WIDTH, HEIGHT = 400, 600
SPEED = 5
SCORE = 0
speed_up = False
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
 
#Create a white screen 
screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("Racer")
 
class Enemy(pygame.sprite.Sprite): # class Enemy car
    #Initialzing 
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (randint(40, WIDTH-40), -50)  

    def move(self): # moving down
        global SCORE, SPEED
        self.rect.move_ip(0,SPEED)
        if self.rect.top > HEIGHT: # new spawn
            SPEED += 0.5
            SCORE += 1
            self.rect.center = (randint(40, WIDTH - 40), -50)
    
    def draw(self): # blit image
        screen.blit(self.image, self.rect)
 
 
class Player(pygame.sprite.Sprite):
    #Initialzing 
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (50, 520)
        
    def move(self): # moving left or right
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)

        if pressed_keys[K_RIGHT] and self.rect.right < WIDTH:        
            self.rect.move_ip(5, 0)
        
    def draw(self): # blit image
        screen.blit(self.image, self.rect)


class Road(pygame.sprite.Sprite):
    #Initialzing 
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("road.png"), (WIDTH, HEIGHT))
        self.y = 0
    
    def move(self): # moving down
        self.y += int(SPEED) // 2

        if self.y > HEIGHT: # spawn back
            self.y -= HEIGHT

    def draw(self): # blit image
        screen.blit(self.image, (0, self.y))
        screen.blit(self.image, (0, self.y - HEIGHT))

class Coin(pygame.sprite.Sprite):
    #Initialzing 
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("coin.png"), (30, 30))
        self.image_gold = pygame.transform.scale(pygame.image.load("super_coin.png"), (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (randint(30, WIDTH-30), -30)
        self.coin_cnt = 0
        self.gold_coin = False

    def move(self): # moving down
        self.rect.move_ip(0, 5)

        if self.rect.top > HEIGHT: # new spawn
            self.spawn()

    def draw(self): # blit image
        if self.gold_coin:
            screen.blit(self.image_gold, self.rect)
        else:
            screen.blit(self.image, self.rect)

    def spawn(self):
        if randint(1, 4) == 1:  # spawn gold coin (chance 25%)
            self.gold_coin = True
        else:
            self.gold_coin = False
        self.rect.center = (randint(30, WIDTH-30), -30)

                   
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
ROAD = Road()
C1 = Coin()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(ROAD)
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():  
        if event.type == QUIT:
            exit()
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.draw()
        entity.move()

    #Text score and coins
    scores = font_small.render(f'scores: {SCORE}', True, WHITE)
    screen.blit(scores, (10, 10))
    screen.blit(font_small.render(f'coins: {C1.coin_cnt}', 1, WHITE), (WIDTH - 90, 10))
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        screen.fill(RED)

        game_over = font.render("Game Over", True, WHITE)
        screen.blit(game_over, (30,250))
        screen.blit(font.render(f'Total: {C1.coin_cnt}', 1, WHITE), (80, 350))
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        exit()

    # collision P1 with coin
    if pygame.sprite.spritecollideany(P1, coins):
        if C1.gold_coin:
            C1.coin_cnt += 3
        else:
            C1.coin_cnt += 1
        C1.spawn()

    # speed up when total coins == 10
    if C1.coin_cnt == 10 and not speed_up:
        SPEED += 2
        speed_up = True

    # display FPS and update
    FramePerSec.tick(60)    
    pygame.display.update()