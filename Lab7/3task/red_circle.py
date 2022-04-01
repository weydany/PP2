import pygame as pg
pg.init()

WIDTH, HEIGHT = 600, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Red Circle')

WHITE = (255, 255, 255)
RED = (255, 0, 0)

FPS = pg.time.Clock()

class Circle:
    x = 300
    y = 300
    radius = 25
    lenght = 50

    def draw(self):
        pg.draw.circle(screen, RED, (self.x, self.y), self.radius)

    def move(self):

        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            for i in range(20):
                if self.y - self.radius > 0:
                    self.y -= 1
        if keys[pg.K_DOWN]:
            for i in range(20):
                if self.y + self.radius <= HEIGHT:
                    self.y += 1
        if keys[pg.K_LEFT]:
            for i in range(20):
                if self.x - self.radius > 0:
                    self.x -= 1
        if keys[pg.K_RIGHT]:
            for i in range(20):
                if self.x + self.radius < WIDTH:
                    self.x += 1

circle = Circle()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    screen.fill(WHITE)

    circle.draw()
    circle.move()

    FPS.tick(50)
    pg.display.update()