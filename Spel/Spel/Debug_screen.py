﻿from ButtonClass import Button
import pygame
import config
import Turn_Order

white = (255,255,255)
cyan = (0,255,255)

fontsize = 30

indentation = 20

Line_Title = Button("Debug screen, press F3 to close", white, font_size =  fontsize)

Line_mousepos = Button("", white, font_size = fontsize)
Line_Tile = Button("", white, font_size = fontsize)
Line_Tile_Biome = Button("", white, font_size = fontsize)
Line_Tile_Owner = Button("", white, font_size = fontsize)
Line_Tile_Troops = Button("", white, font_size = fontsize)
Line_Tile_Building = Button("", white, font_size = fontsize)
Line_Active_Player = Button("", cyan, font_size = fontsize)

def Calculations():
    mouseposition = pygame.mouse.get_pos()
    Line_mousepos.text = "Mouse position:" + str(mouseposition)
    currentplayer = config.PlayerIndex
    current_tile = (int((mouseposition[0]-config.Gameboard_offsetx)/50), int((mouseposition[1]-config.Gameboard_offsety)/50))
    
    if current_tile[0] >= 0 and current_tile[1] >= 0 and current_tile[0] <=17 and current_tile[1] <= 17:
        Line_Tile.text = "Tile: " + str(current_tile)
        Tile_selected = config.mapArray [current_tile[0]] [current_tile[1]]

        if Tile_selected.biome == "w":
            Line_Tile_Biome.text = "Biome: Water"
        elif Tile_selected.biome == "d":
            Line_Tile_Biome.text = "Biome: Desert"
        elif Tile_selected.biome == "i":
            Line_Tile_Biome.text = "Biome: Ice"
        elif Tile_selected.biome == "s":
            Line_Tile_Biome.text = "Biome: Swamp"
        elif Tile_selected.biome == "f":
            Line_Tile_Biome.text = "Biome: Forest"
        else:
            Line_Tile_Biome.text = "Biome: Gems"
        

        if Tile_selected.owner != None:
            Line_Tile_Owner.text = "Owner: " + str(Tile_selected.owner)
        else:
            Line_Tile_Owner.text = "Owner: None"
        
            
        if Tile_selected.troops != []:
            string = ""
            for i in Tile_selected.troops:
                string += i.Name
                string += ", "
            Line_Tile_Troops.text = "Troops: " + string
        else:
            Line_Tile_Troops.text = "Troops: None"


        if Tile_selected.building != None:
            Line_Tile_Building.text = "Building: " + str(Tile_selected.building.Name)
        else:
            Line_Tile_Building.text = "Building: None"

        if Line_Active_Player.text != None:
            Line_Active_Player.text = "Active Player: " + str(config.PlayerIndex + 1)
        else:
            Line_Active_Player.text = "Active Player: None"

    else:
        Line_Tile.text = "Tile: None"
        Line_Tile_Biome.text = ""
        Line_Tile_Owner.text = ""
        Line_Tile_Troops.text = ""
        Line_Tile_Building.text = ""


def Draw(pos):
    Calculations()
    posx = pos[0]
    posy = pos[1]
    pygame.draw.rect(config.setDisplay, (0,0,0), (pos[0], pos[1], 500, 200))
    Line_Title.draw(posx, posy, config.setDisplay)
    size = Line_Title.size()
    posy += size[1]
    Line_mousepos.draw(posx, posy, config.setDisplay)
    size = Line_mousepos.size()
    posy += size[1]
    Line_Tile.draw(posx, posy, config.setDisplay)
    size = Line_Tile.size()
    posy += size[1]
    Line_Tile_Biome.draw(posx+indentation, posy, config.setDisplay)
    size = Line_Tile_Biome.size()
    posy += size[1]
    Line_Tile_Owner.draw(posx+indentation, posy, config.setDisplay)
    size = Line_Tile_Owner.size()
    posy += size[1]
    Line_Tile_Troops.draw(posx+indentation, posy, config.setDisplay)
    size = Line_Tile_Troops.size()
    posy += size[1]
    Line_Tile_Building.draw(posx+indentation, posy, config.setDisplay)
    size = Line_Tile_Building.size()
    posy += size[1]
    Line_Active_Player.draw(posx+indentation, posy, config.setDisplay)
    size = Line_Active_Player.size()
    posy += size[1]

