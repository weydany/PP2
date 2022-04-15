import pygame
from colors import *

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font('font.ttf', 20)
color = BLACK

picked_tool = 'Line'
start_pos = (-5, -5)
end_pos = (-5, -5)

class Tool(pygame.sprite.Sprite):
    
    def __init__(self, x, y, text):
        super().__init__()
        self.x = x
        self.y = y
        self.text = text
        self.picked = False

    def draw(self):
        screen.blit(font.render(self.text, 1, BLACK), (self.x, self.y))
        if self.picked:
            pygame.draw.rect(screen, BLACK, (self.x + 70, self.y + 8, 15, 15))
        else:
            pygame.draw.rect(screen, BLACK, (self.x + 70, self.y + 8, 15, 15), 3)

line = Tool(20, 100, 'Line')
rect = Tool(20, 160, 'Rect')
ellipse = Tool(20, 220, 'Ellipse')
brush = Tool(20, 280, 'Brush')

screen.fill(WHITE)

def main():
    global picked_tool, color
    
    FPS = pygame.time.Clock()
    
    while True:
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = pygame.mouse.get_pos()
                mx, my = start_pos

                # change tool
                if line.x + 70 <= mx <= line.x + 85 and line.y + 8 <= my <= line.y + 23:
                    picked_tool = 'Line'
                elif rect.x + 70 <= mx <= rect.x + 85 and rect.y + 8 <= my <= rect.y + 23:
                    picked_tool = 'Rect'
                elif ellipse.x + 70 <= mx <= ellipse.x + 85 and ellipse.y + 8 <= my <= ellipse.y + 23:
                    picked_tool = 'Ellipse'
                elif brush.x + 70 <= mx <= brush.x + 85 and brush.y + 8 <= my <= brush.y + 23:
                    picked_tool = 'Brush'

                # color pick 
                elif 40 <= mx <= 60 and 360 <= my <= 380:
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

            if event.type == pygame.MOUSEBUTTONUP:
                end_pos = pygame.mouse.get_pos()

                if picked_tool == 'Rect':
                    drawRect(start_pos, end_pos)

                if picked_tool == 'Ellipse':
                    drawEllipse(start_pos, end_pos)
                    
            
            
            if event.type == pygame.MOUSEMOTION and picked_tool == 'Line':
                drawLine()

            if event.type == pygame.MOUSEMOTION and picked_tool == 'Brush':
                useBrush()

        draw_tool_bar(screen)

        pygame.display.update()

        FPS.tick(200)

def drawLine():
    global start_pos
    end_pos = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:
        pygame.draw.line(screen, color, start_pos, end_pos, 3)

    start_pos = end_pos

def useBrush():

    if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, WHITE, mouse_pos, 20)


def drawRect(start_pos, end_pos):
    pygame.draw.rect(screen, color, (end_pos[0], end_pos[1], start_pos[0] - end_pos[0], start_pos[1] - end_pos[1]))
    pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
    pygame.draw.rect(screen, color, (start_pos[0], end_pos[1], end_pos[0] - start_pos[0], start_pos[1] - end_pos[1]))
    pygame.draw.rect(screen, color, (end_pos[0], start_pos[1], start_pos[0] - end_pos[0], end_pos[1] - start_pos[1]))

def drawEllipse(start_pos, end_pos):
    pygame.draw.ellipse(screen, color, (end_pos[0], end_pos[1], start_pos[0] - end_pos[0], start_pos[1] - end_pos[1]))
    pygame.draw.ellipse(screen, color, (start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
    pygame.draw.ellipse(screen, color, (start_pos[0], end_pos[1], end_pos[0] - start_pos[0], start_pos[1] - end_pos[1]))
    pygame.draw.ellipse(screen, color, (end_pos[0], start_pos[1], start_pos[0] - end_pos[0], end_pos[1] - start_pos[1]))



def draw_tool_bar(screen):

    pygame.draw.rect(screen, W_BLUE, (0, 0, 150, HEIGHT))
    

    for tool in [line, rect, ellipse, brush]:
        tool.draw()
        if tool.text == picked_tool:
            tool.picked = True
        else:
            tool.picked = False

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

    pygame.draw.rect(screen, color, (50, 490, 40, 40))
            

main()