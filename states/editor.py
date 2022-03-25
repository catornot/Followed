from states.state import State
from level import Level
from utils import *

class Editor(State):
    def setup(self):
        self.level = Level()
        self.level_name = GenerateBlankLevel( "edited" )
        self.level.loadLevelByName( self.level_name )
        self.level.loadLevelByName("testlevel")
        self.level.SetExit( -2,-1 )
        self.level.SetTwin( -3,-1 )
        self.level.SetPlayer( -1,-1 )
        self.KeysToFunctions = {
            1:self.level.addBoundaries,
            2:self.level.addTrap,
            3:self.level.addKey,
            4:self.level.SetPlayer,
            5:self.level.SetTwin,
            6:self.level.SetExit,
            7:lambda x,y: x+y,
            8:lambda x,y: x+y,
            9:lambda x,y: x+y,
            0:lambda x,y: x+y
        }
        self.current_function = lambda x,y: x+y # blank function


    def update(self, events):

        for i in range(10):
            if events.get( str(i) ):
                self.current_function = self.KeysToFunctions[ i ]
                self.manager.music["select"].play()
        
        if events.get("mousebuttondown"):
            if events["mousebuttondown"].button == 1:
                closestPostion = mouseToGrid()
                self.current_function( closestPostion[0],closestPostion[1] )
                self.manager.music["select"].play()

            elif events["mousebuttondown"].button == 3:
                self.manager.music["select"].play()
                self.level.RemoveBlockByPosition( mouseToGrid() )
        
        if events.get("level"):
            self.manager.music["select"].play()
            self.manager.transition_to("menu")
        
        if events.get("save"):
            self.manager.music["select"].play()
            self.save_level()



    def render(self, surface):
        self.level.render(surface)

    def save_level( self ) -> None:
        LevelStruct = self.level.GetAsDict()
        GridToSave = MakeEmptyGridList()