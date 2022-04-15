import pygame as pg
from random import randrange
from colors import *
from labirinth import *

pg.init()

# settings
WIDTH, HEIGHT = 600, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
FPS = pg.time.Clock()
font = pg.font.SysFont('arial', 20)

# variables
points, level = 0, 1
speed = 10
game = True
change_level = False

class Snake(pg.sprite.Sprite):
    head = [60, 100]
    body = [[60, 80], [60, 60], [60, 40]]
    cur_path = 's' # directory

    def draw(self): # snake drawing
        pg.draw.rect(screen, BLUE, (self.head[0], self.head[1], 20, 20))
        for b in self.body:
            pg.draw.rect(screen, GREEN, (b[0], b[1], 20, 20))

    def rotate(self, path): # changing directory
        if path == 'w' and self.cur_path != 's':
            self.cur_path = 'w'
        elif path == 'a' and self.cur_path != 'd':
            self.cur_path = 'a'
        elif path == 's' and self.cur_path != 'w':
            self.cur_path = 's'
        elif path == 'd' and self.cur_path != 'a':
            self.cur_path = 'd'

    def move(self):
        head_pos = [self.head[0], self.head[1]]
        if self.cur_path == 's': # moving by directory
            self.head[1] += 20
        elif self.cur_path == 'w':
            self.head[1] -= 20
        elif self.cur_path == 'a':
            self.head[0] -= 20
        elif self.cur_path == 'd':
            self.head[0] += 20

        self.body.pop( len(self.body) - 1 )
        self.body.insert(0, head_pos)

    def eating(self, food): # func on eating
        global points
        if food.x == self.head[0] and food.y == self.head[1]: # check collision
            points += 1
            new_body = self.body[-1]
            self.body.append(new_body)
            food.spawn()

snake = Snake()

class Food(pg.sprite.Sprite):
    x = randrange(0, WIDTH, 20) # random point
    y = randrange(0, HEIGHT, 20)
    # random points till points in walls or snake
    while [x, y] in labirinth + labirinth2 + snake.body:
        x = randrange(0, WIDTH, 20)
        y = randrange(0, HEIGHT, 20)

    def draw(self): # food drawing
        pg.draw.rect(screen, YELLOW, (self.x, self.y, 20, 20))

    def spawn(self): # spawn new food when eating
        global speed
        self.x = randrange(0, WIDTH, 20)
        self.y = randrange(0, HEIGHT, 20)
        while [self.x, self.y] in labirinth + labirinth2 + snake.body:
            self.x = randrange(0, WIDTH, 20)
            self.y = randrange(0, HEIGHT, 20)

food = Food()

def game_over():
    global game
    if snake.head in snake.body or snake.head in labirinth: # check collision
        game = False
    elif level == 2 and snake.head in labirinth2: # check collision on second level
        game = False

    # checking out of area
    elif snake.head[0] < 0: 
        game = False
    elif snake.head[0] >= WIDTH:
        game = False
    elif snake.head[1] < 0:
        game = False
    elif snake.head[1] >= HEIGHT:
        game = False

def draw_labirinth(): # drawing walls
    for wall in labirinth:
        pg.draw.rect(screen, BLACK, (wall[0], wall[1], 20, 20))

    if level == 2:
        for wall in labirinth2:
            pg.draw.rect(screen, BLACK, (wall[0], wall[1], 20, 20))

def level_up(): # func to level up from 1 to 2
    global level, speed
    snake.head = [60, 100] # setting default settings
    snake.body = [[60, 80], [60, 60], [60, 40]]
    snake.cur_path = 's'
    level = 2
    speed = 15

while game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
        if event.type == pg.KEYDOWN: # checking key down
            if event.key == pg.K_w:
                snake.rotate('w')
            elif event.key == pg.K_a:
                snake.rotate('a')
            elif event.key == pg.K_s:
                snake.rotate('s')
            elif event.key == pg.K_d:
                snake.rotate('d')

    screen.fill(WHITE) # filling area

    ################### methods of classes
    food.draw()
    snake.move()
    snake.draw()
    snake.eating(food)
    ###################

    draw_labirinth() # functions
    game_over()

    #score and level
    screen.blit(font.render(f'Score: {points}', 1, BLACK), (20, 570))
    screen.blit(font.render(f'Level: {level}', 1, BLACK), (530, 570))

    if points == 10 and not change_level: # checking when we will level up
        change_level = True
        level_up()

    FPS.tick(speed) # game speed (FPS)
    pg.display.update() # updating screen