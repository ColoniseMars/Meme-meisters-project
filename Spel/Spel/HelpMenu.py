﻿import pygame
from ButtonClass import *
import config
import os
import sys
import Music
import Graphics_game

frame = pygame.image.load("textures/Gamerule2.png")

MenuHeight = 950
MenuWidth = 800
numofbuttons = 4
buttonlist = ["Game Rules", "", "", "Resume Game"]
fontsize = 40
padding = 20

Background = Button("", (255,255,255), bgcolor = (99,151,237), height = MenuHeight, width = MenuWidth)
Button1 = Button(buttonlist[0], (0,0,0), bgcolor = (57, 123, 232), font = "algerian", font_size= fontsize, height = MenuHeight/numofbuttons-padding, width = MenuWidth-padding)
Button2 = Button(buttonlist[1], (0,0,0), bgcolor = (57, 123, 232), font_size = fontsize, height = MenuHeight/numofbuttons-padding, width = MenuWidth-padding)
Button3 = Button(buttonlist[2], (0,0,0), bgcolor = (57, 123, 232), font_size = fontsize, height = MenuHeight/numofbuttons-padding, width = MenuWidth-padding)
Button4 = Button(buttonlist[3], (0,0,0), bgcolor = (57, 123, 232), font_size = fontsize, height = MenuHeight/numofbuttons-padding, width = MenuWidth-padding)


def Help_Menu_Draw(position, screen):
    Background.draw(position[0], position[1], screen)
    Button1.draw(position[0]+padding/2, position[1]+padding/2, screen)
    Button2.draw(position[0]+padding/2, position[1]+MenuHeight/numofbuttons+padding/2, screen)
    Button3.draw(position[0]+padding/2, position[1]+MenuHeight/numofbuttons*2+padding/2, screen)
    Button4.draw(position[0]+padding/2, position[1]+MenuHeight/numofbuttons*3+padding/2, screen)
    config.setDisplay.blit(frame, (360, 200))

def HelpM_detect_presses():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            stateMouse = pygame.mouse.get_pressed()
            if stateMouse[0] == 1:
#                if Button1.pressed():
#                    print("Button 1 pressed")
#                    config.window = "MainMenu"
#                    config.firsttime = True
#                if Button2.pressed():
#                    print("No functionaility for this button yet")
#                if Button3.pressed():
#                    pygame.quit()
#                    sys.exit()
                if Button4.pressed():
                    config.window = "Main"
                    config.firsttime = True


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                config.window = "Main"
                config.firsttime = True


        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()