﻿import pygame
import time
import Graphics_game
import config
import ButtonClass
import Music

pygame.init()

display_width = 1500
display_height = 1000

black = (0,0,0)
white = (255,255,255)
#colors are in a range of 0-255 (256 different entries)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_yellow = (239,254,54)
bright_blue = (64,132,244)
red = (200,0,0)
green = (0,200,0)
yellow = (236,220,26)
blue = (11,83,202)
mudgreen = (51,125,2)
mudyellow = (119,117,19)
mudred = (112,46,27)
mudblue = (1,66,137)
magenta = (255,0,255)
gray = (129,126,97)
mudorange = (120,95,7)
mudgray = (2,71,55)
weirdbrown = (169,78,16)


fontsize = 20
#pygame.mixer.music.load("Title.mp3")

BGMOn = ButtonClass.Button("On", black, font = "algerian", font_size = 30, bgcolor = green, height = 88, width = 88)
BGMOff = ButtonClass.Button("Off", black, font = "algerian", font_size = 30, bgcolor = red, height = 88, width = 88)
BGMusic = ButtonClass.Button("Background Music On/Off?", white, font = "algerian", font_size = 40)
MainMenu = ButtonClass.Button("Main Menu", black, font = "algerian", font_size = 20, bgcolor = weirdbrown, height = 80, width = 180)

def quitgame():
    pygame.quit()
    quit()

#gameDisplay = pygame.display.set_mode((display_width,display_height))
#pygame.display.set_caption("Frequency")
#clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    #print(mouse)
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(config.setDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()
##            if action == "play":
##                game_loop()
##            elif action == "quit":
##                pygame.quit()
##                quit()
    else:
        pygame.draw.rect(config.setDisplay, ic, (x,y,w,h))

    smallText = pygame.font.SysFont("algerian",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    config.setDisplay.blit(textSurf, textRect)

def thirdscreen():
    config.window="PlayerNameMenu"
    config.firsttime = True

def settingscreen():

    #intro = True

    #while intro:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if BGMOn.pressed():
                config.music = True
                Music.MenuMusic()
            if BGMOff.pressed():
                config.music = False
                pygame.mixer.music.stop()
            if MainMenu.pressed():
                config.window="MainMenu"
                config.firsttime = False                

    Graphics_game.draw_background()
    BGMOn.draw(1000,300,config.setDisplay)
    MainMenu.draw(135,830,config.setDisplay)
    BGMOff.draw(1115,300,config.setDisplay)
    BGMusic.draw(840,200,config.setDisplay)
    #Graphics_game.draw_socialmedia((1200,800))
    largeText = pygame.font.SysFont("algerian",90)
    TextSurf, TextRect = text_objects("Frequency", largeText)
    TextRect.center = ((display_width/4),(display_height/6))

    config.setDisplay.blit(TextSurf, TextRect)


   # button("New Game",500,450,500,150,green,bright_green,secondscreen)
   # button("Quit",780,780,100,100,red,bright_red,quitgame)
   # button("Load Game",600,650,300,80,yellow,bright_yellow,quitgame)
   # button("Settings",620,780,100,100,blue,bright_blue,quitgame)
        
    #pygame.draw.rect(gameDisplay, red, (500,450,100,50))
    #if 500+100 > mouse[0] > 500 and 450+50 > mouse[1] > 450:
        #pygame.draw.rect(gameDisplay, bright_red, (500,450,100,50))
    #else:
        #pygame.draw.rect(gameDisplay, red, (500,450,100,50))

    #pygame.display.update()
    #clock.tick(15)

#game_intro()
#pygame.quit()
#quit()
#