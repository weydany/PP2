# imports
import pygame as pg
from random import randrange, randint
from colors import *
from labirinth import *
import datetime
from config import con, cursor

pg.init() # initialization

# settings
WIDTH, HEIGHT = 600, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
FPS = pg.time.Clock()
font = pg.font.SysFont('arial', 20)
font_big = pg.font.SysFont('arial', 80)
starttime = datetime.datetime.now()

# variables
points, level = 0, 1
speed = 10
game = True
change_level = False
page = 0
username = ''
# 0 login
# 1 game
# 2 gameover

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

    def eating(self, f, ft): # func on eating
        global points, starttime
        if [f.x, f.y] == self.head: # check collision with food
            if f.super_food:
                points += 5
            else:
                points += 1
                
            new_body = self.body[-1]
            self.body.append(new_body)
            f.spawn()
        
        if [ft.x, ft.y] == self.head: # check collision with food temp
            points += 2
            ft.letsgo = False
            new_body = self.body[-1]
            self.body.append(new_body)
            starttime = datetime.datetime.now()

snake = Snake()

class Food(pg.sprite.Sprite):
    x = randrange(0, WIDTH, 20) # random point
    y = randrange(0, HEIGHT, 20)
    # random points till points in walls or snake
    while [x, y] in labirinth + labirinth2 + snake.body:
        x = randrange(0, WIDTH, 20)
        y = randrange(0, HEIGHT, 20)

    super_food = False

    def draw(self): # food drawing
        if self.super_food: 
            pg.draw.rect(screen, RED, (self.x, self.y, 20, 20))
        else:
            pg.draw.rect(screen, YELLOW, (self.x, self.y, 20, 20))

    def spawn(self): # spawn new food when eating
        global speed
        if randint(1, 8) == 4:
            self.super_food = True
        else:
            self.super_food = False

        self.x = randrange(0, WIDTH, 20)
        self.y = randrange(0, HEIGHT, 20)
        while [self.x, self.y] in labirinth + labirinth2 + snake.body:
            self.x = randrange(0, WIDTH, 20)
            self.y = randrange(0, HEIGHT, 20)

food = Food()

class Food_temp(Food):
    x = randrange(0, WIDTH, 20) # random point
    y = randrange(0, HEIGHT, 20)
    # random points till points in walls or snake
    while [x, y] in labirinth + labirinth2 + snake.body + [[food.x + food.y]]:
        x = randrange(0, WIDTH, 20)
        y = randrange(0, HEIGHT, 20)

    letsgo = False

    def draw(self): # food drawing
        pg.draw.rect(screen, PURPLE, (self.x, self.y, 20, 20))
    
    def spawn(self): # spawn new food temp
        self.x = randrange(0, WIDTH, 20)
        self.y = randrange(0, HEIGHT, 20)
        while [self.x, self.y] in labirinth + labirinth2 + snake.body + [[food.x + food.y]]:
            self.x = randrange(0, WIDTH, 20)
            self.y = randrange(0, HEIGHT, 20)

    
food_temp = Food_temp()

def drop_user():
    cursor.execute(f"""
        DELETE FROM users
        WHERE username = '{username}';

        DELETE FROM user_score
        WHERE user_name = '{username}';

        DELETE FROM game_result
        WHERE username = '{username}';

        DELETE FROM body
        WHERE username = '{username}';
    """)

    con.commit()

def get_result():
    cursor.execute(f"""
        SELECT username FROM users
        WHERE username = '{username}';
    """)
    if len(cursor.fetchall()) != 0:
        cursor.execute(f"""
            SELECT score FROM user_score
            WHERE user_name = '{username}';
        """)
        points = cursor.fetchone()[0]
        

        cursor.execute(f"""
            SELECT * FROM game_result
            WHERE username = '{username}';
        """)

        row = cursor.fetchone()
        level = row[1]
        snake.head = [row[2], row[3]]
        food.x, food.y = row[4], row[5]
        snake.cur_path = row[6]

        cursor.execute(f"""
            SELECT body_x, body_y FROM body
            WHERE username = '{username}';
        """)

        rows = cursor.fetchall()
        snake.body = []
        for row in rows:
            snake.body.append([row[0], row[1]])

def insert_result():
    cursor.execute('SELECT * FROM users;')
    table_users = cursor.fetchall()
    if len(table_users) == 0:
        id = 0
    else:
        id = table_users[-1][0] + 1

    cursor.execute(f"""
        INSERT INTO users(id, username)
        VALUES ({id}, '{username}');

        INSERT INTO user_score(user_name, score)
        VALUES ('{username}', {points});

        INSERT INTO game_result(username, level, head_x, head_y, food_x, food_y, path)
        VALUES ('{username}', {level}, {snake.head[0]}, {snake.head[1]}, {food.x}, {food.y}, '{snake.cur_path}');
    """)

    for body in snake.body:
        cursor.execute(f"""
            INSERT INTO body (username, body_x, body_y)
            VALUES ('{username}', {body[0]}, {body[1]});
        """)

    con.commit()

def game_over():
    global game
    if snake.head in snake.body or snake.head in labirinth: # check collision
        game = False
        drop_user()
    elif level == 2 and snake.head in labirinth2: # check collision on second level
        game = False
        drop_user()

    # checking out of area
    elif snake.head[0] < 0: 
        game = False
        drop_user()
    elif snake.head[0] >= WIDTH:
        game = False
        drop_user()
    elif snake.head[1] < 0:
        game = False
        drop_user()
    elif snake.head[1] >= HEIGHT:
        game = False
        drop_user()

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
    speed = 13

while game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            cursor.execute(f"""
                SELECT username FROM users
                WHERE username = '{username}';
            """)
            if len(cursor.fetchall()) != 0:
                drop_user()
                print('done')

            insert_result()
            game = False
        if event.type == pg.KEYDOWN: # checking key down
            if page == 1:
                if event.key == pg.K_w:
                    snake.rotate('w')
                elif event.key == pg.K_a:
                    snake.rotate('a')
                elif event.key == pg.K_s:
                    snake.rotate('s')
                elif event.key == pg.K_d:
                    snake.rotate('d')
                elif event.key == pg.K_SPACE:
                    page = 2
            elif page == 2:
                if event.key == pg.K_SPACE:
                    page = 1
                    get_result()
            elif page == 0:
                if event.key == pg.K_RETURN:
                    get_result()
                    page = 1

                elif event.key == pg.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode
            

    if page == 0:
        screen.fill(RED)
        pg.draw.rect(screen, WHITE, (200, 280, 200, 40))
        screen.blit(font.render(username, 1, BLACK), (210, 290))


    elif page == 1:
        screen.fill(WHITE) # filling area

        ################### methods of classes
        food.draw()
        if food_temp.letsgo:
            food_temp.draw()
        snake.move()
        snake.draw()
        snake.eating(food, food_temp)
        ###################

        draw_labirinth() # functions
        game_over()

        #score and level
        screen.blit(font.render(f'Score: {points}', 1, BLACK), (20, 570))
        screen.blit(font.render(f'Level: {level}', 1, BLACK), (530, 570))
        screen.blit(font.render(f'user: {username}', 1, BLACK), (10, 10))

        if points >= 15 and not change_level: # checking when we will level up
            change_level = True
            level_up()

        timenow = datetime.datetime.now()

        if (timenow - starttime).total_seconds() >= 10: # if timedelta 10 sec, we spawn food
            starttime = datetime.datetime.now()
            food_temp.letsgo = True

        # if timedelta 5 sec, food temp disappears
        if food_temp.letsgo and (timenow - starttime).total_seconds() >= 5:
            starttime = datetime.datetime.now()
            food_temp.letsgo = False

    elif page == 2:
        screen.fill(YELLOW)
        screen.blit(font_big.render('GAME PAUSED', 1, BLACK), (60, 250))
        drop_user()
        insert_result()


    FPS.tick(speed) # game speed (FPS)
    pg.display.update() # updating screen