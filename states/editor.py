from states.state import State
from level import Level
from utils import *
from pygame import mouse

class Editor(State):
    def __init__(self, manager):
        self.manager = manager

    def setup(self):
        self.level = Level()
        self.level_name = GenerateBlankLevel( "edited" )
        self.level.loadLevelByName( self.level_name )
        # self.level.loadLevelByName("testlevel")

        self.level.SetExit( -2,-1 )
        self.level.SetTwin( -3,-1 )
        self.level.SetPlayer( -1,-1 )

        self.KeysToFunctions = [
            [lambda x,y: x+y, "Nothing"],
            [self.level.addBoundaries, "Boundaries"],
            [self.level.addTrap, "Traps"],
            [self.level.addKey, "Keys"],
            [self.level.SetPlayer, "Player"],
            [self.level.SetTwin, "Twin"],
            [self.level.SetExit, "Exit"],
            [lambda x,y: x+y, "Nothing"],
            [lambda x,y: x+y, "Nothing"],
            [lambda x,y: x+y, "Nothing"]
        ]
        self.selected = "Nothing"
        self.current_function = lambda x,y: x+y # blank function
        self.last_mouse_pos = [0,0]


    def update(self, events):

        for i in range(10):
            if events.get( str(i) ):
                self.current_function = self.KeysToFunctions[ i ][0]
                self.manager.music["select"].play()
                self.selected = self.KeysToFunctions[ i ][1]
        
        if mouse.get_pressed(3)[0]:
            closestPostion = mouseToGrid()
            if self.last_mouse_pos != closestPostion:
                self.current_function( closestPostion[0],closestPostion[1] )
                self.manager.music["select"].play()
                self.last_mouse_pos = closestPostion

        elif mouse.get_pressed(3)[2]:
            mouse_pos = mouseToGrid()
            if self.last_mouse_pos != mouse_pos:
                self.manager.music["select"].play()
                self.level.RemoveBlockByPosition( mouse_pos )
                self.last_mouse_pos = mouse_pos
        
        if events.get("level"):
            self.manager.music["select"].play()
            self.manager.transition_to("menu")
        
        if events.get("save"):
            self.manager.music["select"].play()
            self.save_level()


    def render(self, surface):
        self.level.render(surface)
        self.manager.render_text(surface, f"You have achieved {self.selected}", self.manager.SCREEN_C[0], self.manager.SCREEN_H - 100)


    def save_level( self ) -> None:
        LevelList = self.level.GetAsList()
        GridToSave = MakeEmptyGridList()

        for block in LevelList:
            pos = block.get_pos()
            if pos[0] < 0 or pos[1] < 0:
                continue
            GridToSave[pos[1]][pos[0]] = block.symbol
        
        SavedLevel = ""
        for line in GridToSave:
            Line = ""
            for c in line:
                Line += c
            SavedLevel += f"{Line}\n"
        
        with open(f"levels/{self.level_name}.txt", "w") as file:
            file.write( SavedLevel )