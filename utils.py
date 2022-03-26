from classes.twin import Twin
from classes.exit import Exit
from classes.boundary import Boundary
from classes.trap import Trap
from classes.key import Key
from classes.player import Player
from classes.text import Text
from pygame import mouse
from pygame import mixer
from random import choice
import os

"""
██╗   ██╗████████╗██╗██╗     ███████╗
██║   ██║╚══██╔══╝██║██║     ██╔════╝
██║   ██║   ██║   ██║██║     ███████╗
██║   ██║   ██║   ██║██║     ╚════██║
╚██████╔╝   ██║   ██║███████╗███████║
 ╚═════╝    ╚═╝   ╚═╝╚══════╝╚══════╝
"""

LevelWidth = 30
LevelHeight = 20

def IsKey( entity ):
    return isinstance( entity, Key )

def IsTrap( entity ):
    return isinstance( entity, Trap )

def IsPlayer( entity ):
    return isinstance( entity, Player )

def IsExit( entity ):
    return isinstance( entity, Exit )

def IsTwin( entity ):
    return isinstance( entity, Twin )

def IsBoundary( entity ):
    return isinstance( entity, Boundary )

def IsText( entity ):
    return isinstance( entity, Text )

def IsAPickedUp( entity ):
    return entity.IsPickupable

def HasInventory( entity ):
    return entity.HasInventory

def HasKey( entity ):
    if not HasInventory( entity ):
        return False
    elif entity.inventory["keys"] > 0:
        return True
    return False

def IsKeyActivated( entity ):
    if IsExit( entity ):
        if entity.NeedsKey:
            return True
    return False


def GenerateBlankLevel(level_name:str = "level") -> str:
    """
    This script generates a blank level
    """

    max_level_id = 0

    for root, dirs, files in os.walk( os.path.join( os.getcwd(), "levels" ) ):
        for file in files:
            file = file.split( "." )
            if file[1] == "txt":
                if file[0].startswith( level_name ):
                    max_level_id += 1
    
    BlankLevel = ""

    for y in range(LevelHeight):
        BlankLevel += f'{"0" * LevelWidth }\n'
    
    with open(f"levels/{level_name}{max_level_id}.txt", "w") as file:
        file.write( BlankLevel )
    
    return f"{level_name}{max_level_id}"

def mouseToGrid() -> list:
    mouse_x, mouse_y = mouse.get_pos()
    closestPostion = [100,100]
    for x in range( LevelWidth ):
        for y in range( LevelHeight ): # important if we make the game window dynamic this must be changed
            if 32 > mouse_x - x*32 and 32 > mouse_y - y*32 and 0 <= mouse_x - x*32 and 0 <= mouse_y - y*32:
                closestPostion = [x,y]
    
    return closestPostion

def MakeEmptyGridList() -> list:
    BlankGrid = []
    for y in range(LevelHeight):
        line = []
        for x in range(LevelWidth):
            line.append( "0" )
        BlankGrid.append( line )
    return BlankGrid

class music_manager:
    def __init__(self) -> None:
        self.music = {
            "menu":["assets/music/main_menu.wav"],
            "game":["assets/music/main1.wav","assets/music/main2.wav"]
        }
        self.current_state = ""

    def update( self, state ):
        if mixer.music.get_busy() != True or self.current_state != state:
            mixer.music.fadeout(20)
            for State in self.music.keys():
                if state == State:
                    mixer.music.load( choice(self.music[State]) )
                    mixer.music.play()
                    self.current_state = state
            
            



if __name__ == '__main__':
    GenerateBlankLevel("level")
    