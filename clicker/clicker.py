import pygame
import sys
import time
import csv
pygame.init()
pygame.font.init()
pygame.font.init()
font = pygame.font.SysFont("Arial", 50)
from leaderboard import leader

ut = ""
flag = True
input_rect = pygame.Rect(500, 425, 200, 50)
ut = ''
pygame.mixer.music.load('D:\\bg music.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
leaderboard = pygame.image.load('D:\\leaderboard.png')
moon = pygame.image.load("D:\\moon.webp")
moon.set_colorkey((255, 255, 255))
bg = pygame.image.load("D:\\фон.webp")
bg = pygame.transform.scale(bg, (1200, 1000))
moon = pygame.transform.scale(moon,(140, 140))
from config import *
score = 0
pygame.font.init()
import pygame_widgets
import buttons
start_ticks=pygame.time.get_ticks()
#font = pygame.font.Font("Arial", 50)
import math
pygame.init()
import random
x, y =random.randint(70, 1130), random.randint(70, 930)
pygame.display.set_caption('My clicker')
game_window.blit(bg, (0, 0))
# Our game's Main Loop
running = True
while running:
    if buttons.flag:
         game_window.blit(moon, (x, y))
    for event in pygame.event.get():
        pygame_widgets.update(event)
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        if buttons.miss == 0:
            if buttons.e == 2:
                diff = 'easy'  
            if buttons.e == 1:
                diff = 'normal'
            if buttons.e == 0.5:
                diff = 'hard'
            leader(ut.strip(), score, diff)
            csv_file_path = r'C:\Users\User\Desktop\botik\clicker\leaderboard.csv'  

            with open(r'C:\Users\User\Desktop\botik\clicker\leaderboard.csv', newline='') as f:
                reader = list(csv.reader(f))
            bg2 = pygame.transform.scale(leaderboard, (1200, 1000))
            game_window.blit(bg2, (0, 0))

            leader_text1 = font.render(f'{reader[0][0]}', True, (0, 0, 0))
            game_window.blit(leader_text1, (275, 345))
            leader_text2 = font.render(f'{reader[1][0]}', True, (0, 0, 0))
            game_window.blit(leader_text2, (275, 475))
            leader_text3 = font.render(f'{reader[2][0]}', True, (0, 0, 0))
            game_window.blit(leader_text3, (275, 625))

            leader_score1 = font.render(f'{reader[0][1]}', True, (0, 0, 0))
            game_window.blit(leader_score1, (810, 350))
            leader_score2 = font.render(f'{reader[1][1]}', True, (0, 0, 0))
            game_window.blit(leader_score2, (810, 475))
            leader_score3 = font.render(f'{reader[2][1]}', True, (0, 0, 0))
            game_window.blit(leader_score3, (810, 625))
            pygame.display.update()
            time.sleep(5)
            running = False
        if seconds>buttons.e:
            start_ticks=pygame.time.get_ticks()
            print(seconds)
            x, y = random.randint(140, 1060), random.randint(140, 860)
            game_window.blit(bg, (0, 0))
            if buttons.flag:
                game_window.blit(moon, (x, y))
                pygame.display.update()
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        game_window.blit(score_text, (10, 10))
        attempts_text = font.render(f'Attempts: {buttons.miss}', True, (255, 255, 255))
        game_window.blit(attempts_text, (10, 50))
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            posx = pos[0]
            posy = pos[1]
            c = x + 70
            v = y + 70
            s = math.sqrt(( posx - c)**2 + (posy - v)**2)
            if s <= 70:
                start_ticks=pygame.time.get_ticks()
                x, y = random.randint(140, 1060), random.randint(140, 860)
                game_window.blit(bg, (0, 0))
                game_window.blit(moon, (x, y))
                score += 1
                pygame.display.update()
            if buttons.flag and s > 70:
                buttons.miss -= 1
                pygame.display.update()
        if flag == True:
            pygame.draw.rect(game_window, [255,255,255], input_rect)

            text_surface = font.render(ut, True, (0, 0, 0))
            
            game_window.blit(text_surface, (input_rect.x+5, input_rect.y+5))
            
            input_rect.w = max(100, text_surface.get_width()+10)
        if event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_RETURN:
                flag = False
                buttons.callbutons()
            if event.key == pygame.K_BACKSPACE:
                ut = ut[:-1]
            else:
                ut += event.unicode
        if event.type == pygame.QUIT:
            running = False
            print(buttons.miss)

pygame.quit()