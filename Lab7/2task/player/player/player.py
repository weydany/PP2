import pygame as pg
from pygame import mixer
pg.init()
mixer.init()

WIDTH, HEIGHT = 400, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))

logo = pg.transform.scale(pg.image.load('logo.png'), (280, 280))

current_music = 1
mixer.music.load('songs/song1.mp3')
mixer.music.play()
music = 'Paris - The Chainsmokers'

WHITE = (255, 255, 255)
PURPLE = (180, 0, 255)

class Player:

    playing = True

    def draw(self):
        # play button draw
        pg.draw.circle(screen, WHITE, (WIDTH // 2, 490), 40)

        if not self.playing:
            pg.draw.polygon(screen, PURPLE, [(187, 475), (187, 505), (217, 490)])
        else:
            pg.draw.line(screen, PURPLE, (191, 475), (191, 505), 4)
            pg.draw.line(screen, PURPLE, (205, 475), (205, 505), 4)

        # left button draw
        pg.draw.polygon(screen, WHITE, [(115, 475), (115, 505), (85, 490)])

        # right button draw
        pg.draw.polygon(screen, WHITE, [(285, 475), (285, 505), (315, 490)])

    def play_button(self):
        if self.playing:
            mixer.music.pause()
            self.playing = False
        else:
            mixer.music.unpause()
            self.playing = True

    def left_button(self):
        global current_music
        if current_music == 1:
            current_music = 6
        else:
            current_music -= 1

        mixer.music.load(f'songs/song{current_music}.mp3')
        mixer.music.play()
        self.playing = True


    def right_button(self):
        global current_music
        if current_music == 6:
            current_music = 1
        else:
            current_music += 1

        mixer.music.load(f'songs/song{current_music}.mp3')
        mixer.music.play()
        self.playing = True

    def music_name_set(self):
        global music
        if current_music == 1:
            music = 'Paris - The Chainsmokers'
        elif current_music == 2:
            music = '1-800-273-8255 - Logic'
        elif current_music == 3:
            music = 'Closer - The Chainsmokers'
        elif current_music == 4:
            music = 'Mercy - Shawn Mendes'
        elif current_music == 5:
            music = 'WILD - Troye Sivan'
        elif current_music == 6:
            music = 'Star Boy - The Weekend'


play = Player()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            x = pg.mouse.get_pos()[0]
            y = pg.mouse.get_pos()[1]
            if 160 <= x <= 240 and 450 <= y <= 530:
                play.play_button()

            if 85 <= x <= 115 and 475 <= y <= 505:
                play.left_button()
                play.music_name_set()

            if 285 <= x <= 315 and 475 <= y <= 505:
                play.right_button()
                play.music_name_set()

    screen.fill(PURPLE)
    screen.blit(logo, (60, 50))
    play.draw()

    music_name = music.split(' - ')[0]
    singer = music.split(' - ')[1]

    font = pg.font.Font('font.ttf', 40)
    screen.blit(font.render(music_name, 1, WHITE), (40, 350))
    font = pg.font.Font('font.ttf', 20)
    screen.blit(font.render(singer, 1, WHITE), (40, 400))

    pg.display.update()