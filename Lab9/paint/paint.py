# imports
import pygame
from colors import *

pygame.init() # initilizing

# game settings
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font('font.ttf', 20)
FPS = pygame.time.Clock()

# variables
color = BLACK
picked_tool = 'Line'
start_pos = (-5, -5)
end_pos = (-5, -5)

# Tool class
class Tool(pygame.sprite.Sprite):
    
    def __init__(self, x, y, text):
        super().__init__()
        self.x = x
        self.y = y
        self.text = text
        self.picked = False

    def draw(self): # drawing rect for tools
        screen.blit(font.render(self.text, 1, BLACK), (self.x, self.y))
        if self.picked:
            pygame.draw.rect(screen, BLACK, (self.x + 110, self.y + 8, 15, 15))
        else:
            pygame.draw.rect(screen, BLACK, (self.x + 110, self.y + 8, 15, 15), 3)

# some tools
line = Tool(10, 20, 'Line')
square = Tool(10, 60, 'Square')
rect = Tool(10, 100, 'Rect')
rhombus = Tool(10, 140, 'Rhombus')
ellipse = Tool(10, 180, 'Ellipse')
right_triange = Tool(10, 220, 'Right Tri')
eq_triange = Tool(10, 260, 'Equi Tri')
brush = Tool(10, 300, 'Brush')

def drawLine(): # drawing line by mouse
    global start_pos
    end_pos = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]: # pressed left button
        pygame.draw.line(screen, color, start_pos, end_pos, 3)

    start_pos = end_pos

def useBrush(): # erase by mouse

    if pygame.mouse.get_pressed()[0]: # pressed left button
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, WHITE, mouse_pos, 20)


def drawRect(start_pos, end_pos): # draw rect by mouse
    pygame.draw.rect(screen, color, (end_pos[0], end_pos[1], start_pos[0] - end_pos[0], start_pos[1] - end_pos[1]))
    pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
    pygame.draw.rect(screen, color, (start_pos[0], end_pos[1], end_pos[0] - start_pos[0], start_pos[1] - end_pos[1]))
    pygame.draw.rect(screen, color, (end_pos[0], start_pos[1], start_pos[0] - end_pos[0], end_pos[1] - start_pos[1]))

def drawEllipse(start_pos, end_pos): # draw ellipse by mouse
    pygame.draw.ellipse(screen, color, (end_pos[0], end_pos[1], start_pos[0] - end_pos[0], start_pos[1] - end_pos[1]))
    pygame.draw.ellipse(screen, color, (start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
    pygame.draw.ellipse(screen, color, (start_pos[0], end_pos[1], end_pos[0] - start_pos[0], start_pos[1] - end_pos[1]))
    pygame.draw.ellipse(screen, color, (end_pos[0], start_pos[1], start_pos[0] - end_pos[0], end_pos[1] - start_pos[1]))

def drawSquare(start, end): # draw square by mouse
    width_sq = min(abs(start[0] - end[0]), abs(start[1] - end[1])) # width square
    if start[0] < end[0] and start[1] < end[1]:
        pygame.draw.rect(screen, color, (start[0], start[1], width_sq, width_sq))
    elif start[0] > end[0] and start[1] < end[1]:
        pygame.draw.rect(screen, color, (start[0] - width_sq, start[1], width_sq, width_sq))
    elif start[0] < end[0] and start[1] > end[1]:
        pygame.draw.rect(screen, color, (start[0], end[1], width_sq, width_sq))
    elif start[0] > end[0] and start[1] > end[1]:
        pygame.draw.rect(screen, color, (start[0] - width_sq, end[1], width_sq, width_sq))

def drawRightTriange(s, e): # draw right triangle by 3 points
    
    pygame.draw.polygon(screen, color, ((s[0], s[1]), (e[0], e[1]), (s[0], e[1])))

def drawEquilateralTriange(s, e): # draw equivaletial triangle
    w = abs(s[0] - e[0]) # width of triangle (all)
    h = (w * 3**0.5) / 2 # height of triangle

    if s[1] < e[1]: # if end_pos closer to bottom than start_pos
        pygame.draw.polygon(screen, color, ((e[0], e[1]), (s[0], e[1]), ((s[0] + e[0]) / 2, e[1] - h)))
    else:
        pygame.draw.polygon(screen, color, ((s[0], s[1]), (e[0], s[1]), ((s[0] + e[0]) / 2, s[1] - h)))

def drawRhombus(s, e): # drawing rhombus by mouse

    wx = abs(s[0] - e[0]) / 2 # half width by x
    wy = abs(s[1] - e[1]) / 2 # half width by y

    if s[0] < e[0] and s[1] < e[1]:
        pygame.draw.polygon(screen, color, ((s[0] + wx, s[1]), (s[0], s[1] + wy), (e[0] - wx, e[1]), (e[0], e[1] - wy)))
    elif s[0] > e[0] and s[1] < e[1]:
        pygame.draw.polygon(screen, color, ((s[0] - wx, s[1]), (e[0], e[1] - wy), (e[0] + wx, e[1]), (s[0], s[1] + wy)))
    elif s[0] < e[0] and s[1] > e[1]:
        pygame.draw.polygon(screen, color, ((e[0] - wx, e[1]), (s[0], s[1] - wy), (s[0] + wx, s[1]), (e[0], e[1] + wy)))
    elif s[0] > e[0] and s[1] > e[1]:
        pygame.draw.polygon(screen, color, ((e[0] + wx, e[1]), (e[0], e[1] + wy), (s[0] - wx, s[1]), (s[0], s[1] - wy)))

def draw_tool_bar(): # draw tool bar on the left side

    pygame.draw.rect(screen, W_BLUE, (0, 0, 150, HEIGHT)) # draw background
    

    # drawing tools
    for tool in [line, square, rect, rhombus, ellipse, right_triange, eq_triange, brush]:
        tool.draw()
        if tool.text == picked_tool:
            tool.picked = True
        else:
            tool.picked = False

    # drawing color picker
    i = 1
    for y in range(360, 360+101, 40):
        if i == 1:
            pygame.draw.rect(screen, VIO, (40, y, 20, 20))
            pygame.draw.rect(screen, BLACK, (80, y, 20, 20))

        elif i == 2:
            pygame.draw.rect(screen, BLUE, (40, y, 20, 20))
            pygame.draw.rect(screen, RED, (80, y, 20, 20))

        elif i == 3:
            pygame.draw.rect(screen, GREEN, (40, y, 20, 20))
            pygame.draw.rect(screen, YELLOW, (80, y, 20, 20))

        i += 1

    pygame.draw.rect(screen, color, (50, 490, 40, 40)) # showing picked color
            
screen.fill(WHITE)
while True:
        
    for event in pygame.event.get():
        # determin if X was clicked, or Ctrl+W or Alt+F4 was used
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c: # when button c clicked, screen fill white
                screen.fill(WHITE)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = pygame.mouse.get_pos()
            mx, my = start_pos

            # change tool
            for tool in [line, square, rect, rhombus, ellipse, right_triange, eq_triange, brush]:
                if tool.x + 110 <= mx <= tool.x + 125 and tool.y + 8 <= my <= tool.y + 23:
                    picked_tool = tool.text

            # color pick 
            if 40 <= mx <= 60 and 360 <= my <= 380:
                color = VIO
            elif 80 <= mx <= 100 and 360 <= my <= 380:
                color = BLACK
            elif 40 <= mx <= 60 and 400 <= my <= 420:
                color = BLUE
            elif 80 <= mx <= 100 and 400 <= my <= 420:
                color = RED
            elif 40 <= mx <= 60 and 440 <= my <= 460:
                color = GREEN
            elif 80 <= mx <= 100 and 440 <= my <= 460:
                color = YELLOW

        if event.type == pygame.MOUSEBUTTONUP: # if mouse btn up we draw one of shapes
            end_pos = pygame.mouse.get_pos()

            if picked_tool == 'Rect':
                drawRect(start_pos, end_pos)
            elif picked_tool == 'Ellipse':
                drawEllipse(start_pos, end_pos)
            elif picked_tool == 'Square':
                drawSquare(start_pos, end_pos)
            elif picked_tool == 'Rhombus':
                drawRhombus(start_pos, end_pos)
            elif picked_tool == 'Right Tri':
                drawRightTriange(start_pos, end_pos)
            elif picked_tool == 'Equi Tri':
                drawEquilateralTriange(start_pos, end_pos)
                
        
        # when mouse motion we draw line or use brush
        if event.type == pygame.MOUSEMOTION and picked_tool == 'Line':
            drawLine()

        if event.type == pygame.MOUSEMOTION and picked_tool == 'Brush':
            useBrush()

    draw_tool_bar()

    pygame.display.update()

    FPS.tick(200)